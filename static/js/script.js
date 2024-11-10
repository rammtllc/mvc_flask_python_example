document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("change-greeting");
    const greetingElement = document.getElementById("greeting");

    const greetings = [
        "Hello, World!",
        "Welcome to Flask!",
        "Have a great day!",
        "Stay Awesome!",
        "Flask MVC Rocks!",
    ];

    button.addEventListener("click", () => {
        const randomIndex = Math.floor(Math.random() * greetings.length);
        greetingElement.textContent = greetings[randomIndex];
    });
});
