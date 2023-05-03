currentHTMLelem = document.querySelector(".learning")
translateWord = document.querySelector(".translate")

function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
    return array
}

fetch(`/get-word/`, {
    method: 'POST',
    headers: {},
        body: JSON.stringify({'data': 'myData'})
    })
    .then(response => response.json())
    .then(data => {
        word_list = data.word.split('')
        current_word_list = shuffle(word_list)

//      перевод слова
        current_translate_word = data.trl_word.toUpperCase()
        translateWord.innerHTML += `<div class="trl_word">${current_translate_word}</div>`

        current_word_list.forEach(element => {
            currentHTMLelem.innerHTML += `<div draggable="true" class="word">${element.toUpperCase()}</div>`
        })

//      проверка слов
        const button = document.querySelector('.res__button')
        button.addEventListener('click', elements_list)

        function elements_list(){
            elem_array = document.getElementsByClassName('word')
            check_word = ''
            for (i of elem_array){
                console.log(i.textContent)
                check_word += i.textContent
            }
            console.log(data.word)
            console.log(check_word)

           if (check_word == data.word.toUpperCase()){
               document.getElementById('good_model').classList.add("open")
           }else{
               document.getElementById('bad_model').classList.add("open")
           }

        }

})

