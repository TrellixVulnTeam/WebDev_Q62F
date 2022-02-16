let tasks = document.querySelector('.tasks');
let task = document.querySelectorAll('.task');
let deleteTask = document.querySelectorAll('.delete-button');
let inputText = document.querySelector('.input-field');
let addButton = document.querySelector('.add-button');

function remove(){
    this.parentNode.remove();
}

function addTask(){
    if(inputText.value != null){

        let div = document.createElement("div");
        div.className="task";

        let label = document.createElement("label");
	    label.className = "task-new";

        let check = document.createElement("input");
        check.type = "checkbox";
        check.className = "task-checkbox";

        let span = document.createElement("span");
	    span.innerHTML = inputText.value;

        let deldel = document.createElement("button");
        deldel.className = "delete-button";
        deldel.addEventListener('click', remove);

        tasks.appendChild(div);
        div.appendChild(label);
        label.appendChild(check);
        label.appendChild(span);
        div.appendChild(deldel);

        inputText.value = null;
    }
}



