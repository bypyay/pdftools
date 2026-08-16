<?php
$root = '../../';
$page_title = 'HTML to PDF Converter Online Free | Daily1Step PDF';
$page_description = 'Convert HTML code, rich web pages, or markdown to PDF documents online for free. Custom page sizing and live preview. Processed entirely in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>HTML to PDF</h1>
      <p>Convert HTML markup, styled text, or web notes into clean, printable PDF documents.</p>
    </div>

    <div class="handoff-banner" id="handoffBanner">
      <span>&#10003;</span> <span id="handoffBannerText"></span>
    </div>

    <div style="max-width:980px; margin:20px auto 0;">
      <div style="display:flex; gap:20px; flex-wrap:wrap; margin-bottom:16px;">
        <div style="flex:1; min-width:200px;">
          <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Page Size</label>
          <select id="pageSize" style="width:100%; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:600;">
            <option value="a4" selected>A4 (210 × 297 mm)</option>
            <option value="letter">US Letter (8.5 × 11 in)</option>
            <option value="legal">US Legal</option>
          </select>
        </div>

        <div style="flex:1; min-width:200px;">
          <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Orientation</label>
          <select id="pageOrientation" style="width:100%; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:600;">
            <option value="portrait" selected>Portrait</option>
            <option value="landscape">Landscape</option>
          </select>
        </div>
      </div>

      <div style="display:flex; gap:24px; flex-wrap:wrap;">
        <!-- HTML Code Editor -->
        <div style="flex:1.1; min-width:320px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <label style="font-weight:700; font-size:.9rem; color:var(--ink);">HTML Source Code</label>
            <button type="button" class="preset-chip" id="loadSampleHtmlBtn">Insert Sample Template</button>
          </div>
          <textarea id="htmlInput" rows="18" style="width:100%; padding:14px; border:1.5px solid var(--border); border-radius:10px; font-family:monospace; font-size:.88rem; line-height:1.5; background:var(--bg-soft); color:var(--ink); resize:vertical;"><div style="padding: 24px; font-family: sans-serif; color: #1f2937;">
  <h1 style="color: #e5322d; margin-top:0;">Invoice / Report</h1>
  <p style="color: #6b7280;">Document generated with Daily1Step PDF Tools</p>
  <hr style="border: none; border-top: 2px solid #e5e7eb; margin: 16px 0;">
  <h3>Summary Table</h3>
  <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <tr style="background: #f3f4f6;">
      <th style="padding: 10px; border: 1px solid #d1d5db; text-align: left;">Item</th>
      <th style="padding: 10px; border: 1px solid #d1d5db; text-align: right;">Amount</th>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #d1d5db;">Service Subscription</td>
      <td style="padding: 10px; border: 1px solid #d1d5db; text-align: right;">$49.00</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #d1d5db;">Custom Integration</td>
      <td style="padding: 10px; border: 1px solid #d1d5db; text-align: right;">$150.00</td>
    </tr>
  </table>
  <p style="margin-top: 24px; font-weight: bold;">Thank you for your business!</p>
</div></textarea>
        </div>

        <!-- Live Preview Frame -->
        <div style="flex:1; min-width:300px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Live Visual Preview</label>
          <div id="htmlPreviewCard" style="border:2px solid var(--border); border-radius:10px; min-height:360px; background:#fff; overflow:auto; box-shadow:var(--shadow-sm);">
            <iframe id="htmlPreviewIframe" style="width:100%; height:380px; border:none; display:block;"></iframe>
          </div>
        </div>
      </div>

      <div class="actions" style="margin-top:24px; text-align:center;">
        <button class="btn" id="generatePdfBtn">Convert &amp; Download PDF</button>
      </div>

      <div class="progress-wrap" id="progressWrap" style="display:none;">
        <div class="progress-bar"><div id="progressBar"></div></div>
        <div class="status-text" id="statusText">Generating PDF...</div>
      </div>

      <div class="result-box" id="resultBox" style="display:none;">
        <div class="check">&#10003;</div>
        <h3>Your PDF is ready!</h3>
        <p id="resultInfo"></p>
        <a class="btn" id="downloadPdfLink" download="document.pdf">Download document.pdf</a>
      </div>
    </div>

    <p class="privacy-note" style="margin-top:30px;">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your code and text never leave your device — rendered 100% locally in your browser.
    </p>

    <section class="info-section">
      <h2>How to convert HTML to PDF</h2>
      <ol>
        <li>Paste or type your HTML code into the editor.</li>
        <li>Review the live preview on the right.</li>
        <li>Click <strong>Convert &amp; Download PDF</strong> to get your formatted document.</li>
      </ol>
    </section>
  </div>
</section>

<style>
.preset-chip {
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 3px 10px;
  font-size: .75rem;
  font-weight: 600;
  color: var(--ink-soft);
  cursor: pointer;
  transition: all .15s;
}
.preset-chip:hover {
  background: var(--red-light);
  border-color: var(--red);
  color: var(--red);
}
</style>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/html-to-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
