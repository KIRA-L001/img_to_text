// OCR submission handler for the standalone page.
function submission(event) {
    event.preventDefault();

    let resultshow = document.getElementsByClassName('result')[0];
    resultshow.innerHTML = 'Loading...'
    var formData = new FormData();
    formData.append('image', $('#fileInput')[0].files[0]);
    $.ajax({
        method: 'POST',
        url: 'https://api.api-ninjas.com/v1/imagetotext',
        // API key is loaded from config.js (not committed to the repo)
        headers: {'X-Api-Key': API_NINJAS_KEY},
        data: formData,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function (result) {
            let texts = result.map(item => item.text)
            let text = texts.join(' ')
            resultshow.innerHTML = text;
        },
        error: function ajaxError(jqXHR, textStatus, errorThrown) {
            alert(jqXHR.responseText);
            resultshow.innerHTML = 'Failed to load'
        }
    });
}
let downloadBtn = document.querySelector("#download-btn");

downloadBtn.addEventListener("click", (e) => {
  // fix: was `textTextElem` (undefined) — use the output textarea element
  let outputText = document.querySelector("#output-text").value;
  let outputLanguage =
    outputLanguageDropdown.querySelector(".selected").dataset.value;
  if (outputText) {
    let blob = new Blob([outputText], { type: "text/plain" });
    let url = URL.createObjectURL(blob);
    let a = document.createElement("a");
    a.download = `translated-to-${outputLanguage}.txt`;
    a.href = url;
    a.click();
  }
});
function next(){
    window.location.href = "transtalte.html";
}