

function getRandomInt(min, max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

class Statement {
    constructor(text) {
        this.text = text;
        this.evidences = [];
        this.premises = []; // array of references to other Statement objects
        this.rect = {
            x: getRandomInt(0, canvas.width-150),
            y: getRandomInt(0, canvas.height-100),
            width: 150,
            height: 100,
            isDragging: false
        };
    }


    draw() {
        console.log("drawing", this.text, "at", this.rect.x, this.rect.y);
        // ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.rect(this.rect.x, this.rect.y, this.rect.width, this.rect.height);
        ctx.fillText(this.text, this.rect.x+10, this.rect.y+50);
        ctx.stroke();
    }
    
    mouseOverlap(mouseX, mouseY) {
        if (mouseX > this.rect.x && mouseX < this.rect.x + this.rect.width && mouseY > this.rect.y && mouseY < this.rect.y + this.rect.height) {
            return true;
        }
        return false;
    }
}


const canvas = document.getElementById("myCanvas");
// canvas always fills the window

canvas.width = window.innerWidth; // equals window dimension

canvas.height = window.innerHeight;
window.addEventListener('resize', function () {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    statements.forEach(s => s.draw());
});
const ctx = canvas.getContext("2d");



const statement1 = new Statement("All humans are mortal.");
const statement2 = new Statement("Socrates is a human.");
const statement3 = new Statement("Therefore, Socrates is mortal.");

statement1.evidences.push("This is a well-known fact.");
statement2.evidences.push("This is also a well-known fact.");

statement3.premises.push(statement1, statement2);
statements = [statement1, statement2, statement3];

statements.forEach(s => s.draw());

document.addEventListener('mousedown', function (e) {
    let mouseX = e.clientX - canvas.offsetLeft;
    let mouseY = e.clientY - canvas.offsetTop;

    statements.forEach(s => {
        if (s.mouseOverlap(mouseX, mouseY)) {
            s.rect.isDragging = true;
            s.rect.offsetX = s.rect.x - mouseX;
            s.rect.offsetY = s.rect.y - mouseY;
        }
    });
});
document.addEventListener('mousemove', function (e) {
    dragged = false
    statements.forEach(s => {
        if (s.rect.isDragging) {
            s.rect.x = e.clientX - canvas.offsetLeft + s.rect.offsetX;
            s.rect.y = e.clientY - canvas.offsetTop + s.rect.offsetY;
            dragged = true
        }
    });
    if (dragged) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        statements.forEach(s => s.draw());
    }
});
document.addEventListener('mouseup', function (e) {
    statements.forEach(s => {
        s.rect.isDragging = false;
    });

});
// function draw() {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     ctx.beginPath();
//     ctx.rect(rect.x, rect.y, rect.width, rect.height);
//     ctx.stroke();
// }

// draw();


