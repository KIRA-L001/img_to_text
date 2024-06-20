function submission(event) {
    event.preventDefault();

    let resultshow = document.getElementsByClassName('result')[0];
    resultshow.innerHTML = 'Loading...'
    var formData = new FormData();
    formData.append('image', $('#fileInput')[0].files[0]);
    $.ajax({
        method: 'POST',
        url: 'https://api.api-ninjas.com/v1/imagetotext',
        headers: {'X-Api-Key': 'y+xrzFL0in3iD2tF1plouA==hy4OSpG7B0IlSQUo'},
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
  let outputText = textTextElem.value;
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