const search_input = document.querySelector('#search_input');
const search_box = document.querySelector('#search_box');
const input = document.createElement('input');
const side = document.querySelector('#side');
const box_open = false;

search_input.addEventListener('click', function (event) {
    console.log("검색클릭");
search_box.classList.remove('search-off');
search_box.classList.add('search-on');
const box_open = true;
console.log("검색 열림");

});

document.addEventListener('click', function (e) {
    console.log(e.target)
console.log(search_box.id)
if (box_open === true)
;
{
    if (e.target !== search_input) {
    search_box.classList.remove('search-on');
search_box.classList.add('search-off');
console.log("검색디브 닫힘")
    }
}
});
// 노래검색
window.onload = function () {
    search_input.onkeyup = function () {
        console.log("검색중")
        axios({
            method: 'get',
            url: `/articles/song_search/?search=${search_input.value}`
        })
            .then(response => {
                const search_box = document.querySelector('#search_box');
                const song_list = response.data.song_list;
                search_box.textContent = "";
                for (let i = 0; i < song_list.length; i++) {
                    search_box.insertAdjacentHTML('beforeend', `
    <div onclick="add_song()" data-name-id="${song_list[i].name}"  data-song_name-id="${song_list[i].id}"  id="song_${song_list[i].id}">
    <hr class='m-0'>
        <div class='search-box'  data-name-id="${song_list[i].name}">
        <div class="search-box-mini d-flex align-items-center" data-name-id="${song_list[i].name}">  
            <img onclick="add_keyboard()" data-name-id="${song_list[i].name}" class="search-thumbnail" src="${song_list[i].thumbnail}" style="height: 100px;">
            <div class="ms-3" onclick="add_song()" data-name-id="${song_list[i].name}" >${song_list[i].name}</div> 
        </div>
        </div>
    </div>
    `);
                }
            })
    }
}

const add_song = (e) => {
const add_id = document.querySelector(`#song_${event.target.dataset.songId}`)
search_input.value = `${event.target.dataset.nameId}`
console.log(`${event.target.dataset.nameId}`)
}