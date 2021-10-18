const name = document.querySelector("wired-input");
const button = document.querySelector("wired-button");
button.addEventListener("click", () => {
    // window.alert(`Hello ${name.value.trim()}!`);
    fetch(window.location.origin+'/proxy/8085/setvalue?value='+name.value.trim()+'&variable=monnom')
});    