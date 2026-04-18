const morse = {
    A: ".-", B: "-...", C: "-.-.", D: "-..", E: ".",
    F: "..-.", G: "--.", H: "....", I: "..", J: ".---",
    K: "-.-", L: ".-..", M: "--", N: "-.", O: "---",
    P: ".--.", Q: "--.-", R: ".-.", S: "...", T: "-",
    U: "..-", V: "...-", W: ".--", X: "-..-", Y: "-.--", Z: "--.."
};

function convert() {
    let text = document.getElementById("inputText").value.toUpperCase();
    let result = "";

    for (let char of text) {
        if (morse[char]) {
            result += morse[char] + " ";
        }
    }

    document.getElementById("output").innerText = result;
}