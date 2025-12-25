function renderInput() {
    const input = document.getElementById("input").value;

    // ❌ RENTAN XSS (UNTUK EDUKASI)
    document.getElementById("output").innerHTML =
        `<span>Output:</span> ${input}`;
}
