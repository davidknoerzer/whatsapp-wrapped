const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);

/** @param {Event} event */
function handleSubmit(event) {
  const url = new URL(form.action);
  const formData = new FormData(form);

  /** @type {Parameters<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
    body: formData,
  };

  fetch(url, fetchOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // This returns a promise containing the JSON parsed data
    })
    .then((data) => {
      console.log(data); // Here you log the JSON data returned by your backend
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });

  event.preventDefault();
}
