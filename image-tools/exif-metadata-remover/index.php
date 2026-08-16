<?php
$root = '../../';
$page_title = 'Remove EXIF Metadata Online Free — Strip GPS & Camera Data | Daily1Step';
$page_description = 'Strip GPS location data, camera information, timestamp, and device metadata from JPG/PNG photos for privacy before sharing. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Remove EXIF & GPS Metadata</h1>
      <p>Clean location coordinates, camera models, dates, and device tags to protect your online privacy.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select a photo to clean</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <h4 style="margin:0 0 8px; font-size:1.1rem; color:var(--ink);" id="fileName"></h4>
        <p style="color:var(--ink-soft); font-size:.88rem; margin-bottom:18px;">Photo will be re-encoded on clean canvas with all EXIF headers stripped.</p>

        <button class="btn" id="cleanBtn">Strip Metadata & Download</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/exif-metadata-remover.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
