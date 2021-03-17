const likeButton = document.querySelector('.like');
const likeDiv = document.querySelector('.like-div');
const doc = document.querySelector('.card-content-main');

const toggleLike = async (pk) => {
    const response = await fetch(`togglelike/${pk}`);
    const data = await response.json();
    return data;
}

doc.addEventListener('click', (event) => {
    if(event.target.classList.contains('fa-heart')){
        const id = event.target.getAttribute('data-id');
        
        toggleLike(id).then(response => {
            is_liked = response.is_liked;
            console.log(is_liked);
            if(is_liked){
                event.target.parentElement.innerHTML = `<i data-id=${id} class="fas fa-heart colors"></i>`
            }else{
                event.target.parentElement.innerHTML = `<i data-id=${id} class="far fa-heart"></i>`;
            }
    
        }).catch(err => console.log(err));

    }
});

