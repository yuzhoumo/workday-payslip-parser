# Guide: Automatically Download All Your Workday Payslips

1. Navigate to your company's Workday website and navigate to your payslips.
2. Click the "View" button on your **most recent** payslip.
3. Open the Chrome dev console (`fn+f12` on mac, `f12` on windows).
4. Paste the folllowing javscript into the console and hit enter.

NOTE - Please make sure you read and understand what this script does!! It
is a very bad idea to paste scripts into your browser from strangers without
reading them, and I don't want to encourage that 🙃. I've commented each step
to make it clear:

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
