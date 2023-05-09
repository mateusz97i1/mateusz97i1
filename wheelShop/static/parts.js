
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const offerBloks = entry.target.querySelectorAll('.offerBlok');
        offerBloks.forEach((offerBlok) => {
          offerBlok.classList.add('showEachWheel');
        });
      }
    });
  }, {
    threshold: 0.05
  });
  
  const offerWheels = document.querySelectorAll('.offerWheels');
  offerWheels.forEach((offerWheel) => {
    observer.observe(offerWheel);
  });

 