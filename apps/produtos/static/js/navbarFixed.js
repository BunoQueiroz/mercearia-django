function fixed(navbar){
    window.addEventListener('scroll', () => {
        const { scrollTop, scrollHeight} = document.documentElement;
    
        if(scrollTop > 120 && scrollHeight > 1000){
            navbar.classList.add('fixed', 'py-0')
        } else {
            navbar.classList.remove('fixed', 'py-0')
        }
    });
}
