<?php
$root = '';
$page_title = 'About Daily1Step PDF — Free Online PDF Tools';
$page_description = 'Learn about Daily1Step PDF, a free set of browser-based PDF tools that never upload your files to a server.';
include __DIR__ . '/includes/header.php';
?>
<section class="tool-page">
  <div class="container info-section" style="margin-top:0;">
    <h1>About Daily1Step PDF</h1>
    <p>Daily1Step PDF is a free collection of PDF tools — merge, split, compress and convert — built to work entirely inside your web browser. There's nothing to install and nothing to sign up for.</p>

    <h2>Why we built it this way</h2>
    <p>Most online PDF tools upload your files to a server, process them, and send the result back. Daily1Step PDF takes a different approach: your files are read, processed and turned into a result entirely on your own device using JavaScript. They are never transmitted anywhere. This is faster (no upload/download wait) and more private (nobody but you ever sees your documents).</p>

    <h2>What's the trade-off?</h2>
    <p>Because everything runs in your browser, very large files or very complex documents may take longer to process on lower-powered devices than they would on a server farm — the trade-off is privacy and speed for typical documents versus raw power for extreme edge cases.</p>

    <h2>Get in touch</h2>
    <p>Questions or feedback? Visit our <a href="<?php echo $root; ?>contact.php">Contact page</a>.</p>
  </div>
</section>
<?php include __DIR__ . '/includes/footer.php'; ?>
