
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.querySelector('.fourImages').classList.add('show');
      }
    });
  }, {
    threshold: 0.15
  });
  
  const offer1 = document.querySelector('.offer1');
  observer.observe(offer1);

