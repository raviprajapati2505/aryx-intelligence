import { memo } from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Layout from './components/Layout';
import NotFoundPage from './pages/NotFoundPage';
import { pages } from './pages';

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            ...pages.map((page) => {
                const Component = memo(page.Component);

                return {
                    ...(page.path === '/' ? { index: true } : { path: page.path.slice(1) }),
                    element: <Component />,
                    handle: page.meta,
                };
            }),
            {
                path: '*',
                element: <NotFoundPage />,
                handle: NotFoundPage.meta,
            },
        ],
    },
]);

export default function App() {
    return <RouterProvider router={router} />;
}
