document
  .getElementById("uploadForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append("file", document.getElementById("fileInput").files[0]);

    fetch("/api/whatsapp-wrapped", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        const { emojiRank, monthRank, nameRank } = data;

        console.log(JSON.parse(emojiRank));
        console.log(JSON.parse(monthRank));
        console.log(JSON.parse(nameRank));
      })
      .catch((error) => {
        console.error("Error:", error);
        document.getElementById("response").innerHTML =
          "<p>Error uploading file</p>";
      });
  });
