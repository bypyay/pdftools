<?php
/**
 * Shared header. Pages must set $page_title and $page_description
 * before including this file. $root should be "" for homepage or
 * "../" (etc.) for pages in subfolders, so asset links resolve correctly.
 */
if (!isset($root)) { $root = ''; }
if (!isset($page_title)) { $page_title = 'Daily1Step PDF — Free Online PDF Tools'; }
if (!isset($page_description)) { $page_description = 'Merge, split, compress and convert PDF files online for free. Fast, secure, works in your browser.'; }
if (!isset($canonical)) { $canonical = ''; }
?><!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><?php echo htmlspecialchars($page_title); ?></title>
<meta name="description" content="<?php echo htmlspecialchars($page_description); ?>">
<?php if ($canonical): ?><link rel="canonical" href="<?php echo htmlspecialchars($canonical); ?>"><?php endif; ?>
<meta property="og:title" content="<?php echo htmlspecialchars($page_title); ?>">
<meta property="og:description" content="<?php echo htmlspecialchars($page_description); ?>">
<meta property="og:type" content="website">
<meta name="robots" content="index, follow">
<link rel="icon" href="<?php echo $root; ?>assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="<?php echo $root; ?>assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="<?php echo $root; ?>index.php" class="brand">Daily1Step PDF<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="<?php echo $root; ?>index.php" style="color:var(--red); font-weight:700;">📄 PDF Tools</a>
      <a href="https://bypyay.github.io/imagetools/" target="_blank">🖼️ Image Tools</a>
      <a href="https://bypyay.github.io/audiotools/" target="_blank">🎧 Audio Tools</a>
      <a href="<?php echo $root; ?>tools/merge-pdf/">Merge PDF</a>
      <a href="<?php echo $root; ?>tools/split-pdf/">Split PDF</a>
      <a href="<?php echo $root; ?>tools/compress-pdf/">Compress PDF</a>
      <a href="<?php echo $root; ?>about.php">About</a>
    </nav>
  </div>
</header>
