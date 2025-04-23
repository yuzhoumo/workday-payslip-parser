# Guide: Automatically Download All Your Workday Payslips

1. Go to your company's Workday website and navigate to your payslips list.
2. Click the "View" button on your **most recent** payslip.
3. Open the dev console (`fn+f12` on mac, `f12` on windows).
4. **Allow popups** in your browser, otherwise the downloads will be blocked.
5. Paste the folllowing javscript into the console and hit enter.

Please read this script before running it! It is a bad idea to paste scripts
into your browser from strangers without reading them first 🙃.

```javascript
(async function downloadAllPayslips() {
  const delay = ms => new Promise(res => setTimeout(res, ms));

  while (true) {
    // 1) Find and click the Export-to-Excel button
    const exportBtn = document.querySelector(
      '[data-automation-id="excelIconButton"], [data-uxi-element-id="excelButton"]'
    );
    if (!exportBtn) {
      console.log('🚫 [Step 1] Export button not found – stopping.');
      break;
    }
    exportBtn.click();
    console.log('✅ Clicked Export to Excel');

    // 2) Wait for the Download button to appear, then click it
    await delay(1000);
    const downloadBtn = document.querySelector('[data-automation-id="uic_downloadButton"]');
    if (!downloadBtn) {
      console.log('🚫 [Step 2] Download button not found – stopping.');
      break;
    }
    downloadBtn.click();
    console.log('✅ Clicked Download');

    // 3) Give the download a moment to start
    await delay(2000);

    // 4) Find and click the Previous Payslip button
    const prevBtn = document.querySelector('button[title="Previous Payslip"]');
    if (!prevBtn) {
      console.log('🎉 No more Previous Payslip button – all done!');
      break;
    }
    prevBtn.click();
    console.log('✅ Navigating to previous payslip…');

    // 5) Wait for the new payslip page to load before repeating
    await delay(3000);
  }
})();
```
