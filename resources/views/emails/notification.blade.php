<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{{ $headline }}</title>
</head>
<body style="margin:0;padding:0;background:#ECF1EF;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ECF1EF;margin:0;padding:32px 12px;">
<tr>
<td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#ffffff;border-collapse:collapse;">
<tr>
<td style="background:#061310;padding:28px 36px 24px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td style="font-family:Arial,Helvetica,sans-serif;font-size:13px;letter-spacing:3px;color:#3DD6B0;font-weight:700;">ARYX</td>
<td align="right" style="font-family:Arial,Helvetica,sans-serif;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#87968F;">{{ $kicker }}</td>
</tr>
</table>
<div style="height:3px;background:#3DD6B0;margin-top:22px;width:56px;line-height:3px;font-size:0;">&nbsp;</div>
<h1 style="margin:18px 0 0;font-family:Arial,Helvetica,sans-serif;font-size:28px;line-height:1.25;font-weight:700;color:#F6F8F7;">{{ $headline }}</h1>
</td>
</tr>
<tr>
<td style="padding:28px 36px 8px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6;color:#5F6E68;">
{{ $intro }}
</td>
</tr>
<tr>
<td style="padding:8px 36px 12px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
@foreach ($fields as $label => $value)
<tr>
<td style="padding:12px 0;border-bottom:1px solid #ECF1EF;width:168px;vertical-align:top;font-family:Arial,Helvetica,sans-serif;font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#87968F;">{{ $label }}</td>
<td style="padding:12px 0;border-bottom:1px solid #ECF1EF;vertical-align:top;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.45;color:#171B19;">{{ $value }}</td>
</tr>
@endforeach
</table>
</td>
</tr>
@if (filled($note))
<tr>
<td style="padding:8px 36px 8px;">
<p style="margin:16px 0 8px;font-family:Arial,Helvetica,sans-serif;font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#87968F;">What they need</p>
<div style="background:#F6F8F7;border-left:3px solid #008775;padding:16px 18px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6;color:#171B19;">{!! nl2br(e($note)) !!}</div>
</td>
</tr>
@endif
<tr>
<td style="padding:22px 36px 32px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#87968F;">
Aryx Intelligence · Doha, Qatar<br>
Reply to this message to continue the conversation.
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
