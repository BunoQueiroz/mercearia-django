const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

    if(scrollTop > 120){
        navbar.classList.add('fixed', 'py-0')
    } else {
        navbar.classList.remove('fixed', 'py-0')
    }

});
