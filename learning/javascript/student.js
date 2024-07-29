function result() {
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var gender = document.querySelector('input[name="gender"]:checked')?.value || '';
    var course = document.getElementById("course").value;
    var email = document.getElementById("email").value;

    var tr = document.createElement("tr");
    var tdName = tr.appendChild(document.createElement("td"));
    var tdAge = tr.appendChild(document.createElement("td"));
    var tdGender = tr.appendChild(document.createElement("td"));
    var tdCourse = tr.appendChild(document.createElement("td"));
    var tdEmail = tr.appendChild(document.createElement("td"));
    var tdAction = tr.appendChild(document.createElement("td"));

    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.onclick = function () {
      tr.remove();
    };
    tdAction.appendChild(deleteButton);

    tdName.innerHTML = name;
    tdAge.innerHTML = age;
    tdGender.innerHTML = gender;
    tdCourse.innerHTML = course;
    tdEmail.innerHTML = email;

    document.querySelector("#get tbody").appendChild(tr);
  }