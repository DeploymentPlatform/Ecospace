/* ==========================================================================
   INTERACTION ENGINE: ECO SPACE PRODUCTS (MULTI-PAGE STATIC ROBUST ENGINE)
   Safe-initialized modules built for separate HTML pages. Zero-error console.
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ==========================================================================
     1. ACTIVE PAGE NAVIGATION HIGHLIGHTING (FILENAME MATCHING)
     ========================================================================== */
  const highlightActiveNavLink = () => {
    const path = window.location.pathname;
    let page = path.split('/').pop() || 'index.html';
    
    const validPages = ['index.html', 'alloy.html', 'furniture.html', 'projects.html', 'about.html', 'contact.html'];
    
    // Normalize roots (e.g. folder routes on Github Pages or local drives)
    if (page === '' || page.endsWith('/') || !validPages.includes(page)) {
      page = 'index.html';
    }

    const desktopLinks = document.querySelectorAll('.desktop-nav .nav-item-link, .dropdown-link');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');

    const matchAndHighlight = (links) => {
      links.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        
        // Remove prior active tags
        link.classList.remove('active');

        // Check exact page file matches
        if (href === page) {
          link.classList.add('active');
          
          // Products Dropdown active parent handling (Desktop & Mobile)
          if (link.classList.contains('dropdown-link') || link.classList.contains('sub-link')) {
            const dropdownTrigger = document.querySelector('.dropdown-trigger');
            const mobileDropdownTrigger = document.getElementById('mobile-dropdown-trigger');
            if (dropdownTrigger) dropdownTrigger.classList.add('active');
            if (mobileDropdownTrigger) mobileDropdownTrigger.classList.add('active');
          }
        }
      });
    };

    matchAndHighlight(desktopLinks);
    matchAndHighlight(mobileLinks);
  };

  highlightActiveNavLink();


  /* ==========================================================================
     2. FIXED HEADER STICKY SCROLLS
     ========================================================================== */
  const header = document.getElementById('main-header');
  
  if (header) {
    const handleHeaderScroll = () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    };
    
    window.addEventListener('scroll', handleHeaderScroll);
    handleHeaderScroll();
  }


  /* ==========================================================================
     3. MOBILE DRAWER NAVIGATION MENU
     ========================================================================== */
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const mobileDrawer = document.getElementById('mobile-nav-drawer');
  const mobileDropdownTrigger = document.getElementById('mobile-dropdown-trigger');
  const mobileDropdownMenu = document.getElementById('mobile-dropdown-menu');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      mobileToggle.classList.toggle('active');
      mobileDrawer.classList.toggle('active');
    });
  }

  if (mobileDropdownTrigger && mobileDropdownMenu) {
    mobileDropdownTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      mobileDropdownTrigger.classList.toggle('active');
      mobileDropdownMenu.classList.toggle('active');
    });
  }


  /* ==========================================================================
     4. HERO CAROUSEL MODULE (index.html ONLY)
     ========================================================================== */
  const initHeroCarousel = () => {
    const carouselContainer = document.getElementById('hero-carousel-container');
    if (!carouselContainer) return; // Clean exit if not on index.html

    const heroSlides = carouselContainer.querySelectorAll('.carousel-slide');
    const thumbnailCards = carouselContainer.querySelectorAll('.thumbnail-card');
    const prevBtn = document.getElementById('carousel-prev-btn');
    const nextBtn = document.getElementById('carousel-next-btn');
    
    let currentHeroSlide = 0;
    const slideInterval = 6000;
    let heroTimer = null;

    const showHeroSlide = (index) => {
      if (index >= heroSlides.length) index = 0;
      if (index < 0) index = heroSlides.length - 1;
      
      currentHeroSlide = index;

      heroSlides.forEach((slide, i) => {
        if (i === currentHeroSlide) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      thumbnailCards.forEach((card, i) => {
        const bar = card.querySelector('.progress-fill');
        if (i === currentHeroSlide) {
          card.classList.add('active');
          if (bar) {
            bar.style.animation = 'none';
            bar.offsetHeight; // trigger reflow
            bar.style.animation = '';
          }
        } else {
          card.classList.remove('active');
        }
      });
    };

    const nextHeroSlide = () => showHeroSlide(currentHeroSlide + 1);
    const prevHeroSlide = () => showHeroSlide(currentHeroSlide - 1);

    const startHeroTimer = () => {
      stopHeroTimer();
      heroTimer = setInterval(nextHeroSlide, slideInterval);
    };

    const stopHeroTimer = () => {
      if (heroTimer) clearInterval(heroTimer);
    };

    if (nextBtn) nextBtn.addEventListener('click', () => { nextHeroSlide(); startHeroTimer(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevHeroSlide(); startHeroTimer(); });

    thumbnailCards.forEach((card, index) => {
      card.addEventListener('click', () => {
        showHeroSlide(index);
        startHeroTimer();
      });
    });

    // Keyboard support
    document.addEventListener('keydown', (e) => {
      if (window.scrollY < window.innerHeight) {
        if (e.key === 'ArrowRight') {
          nextHeroSlide();
          startHeroTimer();
        } else if (e.key === 'ArrowLeft') {
          prevHeroSlide();
          startHeroTimer();
        }
      }
    });

    // Pause on hover
    carouselContainer.addEventListener('mouseenter', stopHeroTimer);
    carouselContainer.addEventListener('mouseleave', startHeroTimer);

    // Initial trigger
    showHeroSlide(0);
    startHeroTimer();
  };

  initHeroCarousel();


  /* ==========================================================================
     5. PARTITIONS FADING SIDEBAR SLIDESHOW (alloy.html ONLY)
     ========================================================================== */
  const initAlloySlideshow = () => {
    const slideshowContainer = document.getElementById('alloy-slideshow-images');
    if (!slideshowContainer) return; // Clean exit if not on alloy.html

    const alloySlides = slideshowContainer.querySelectorAll('.slideshow-img');
    const alloyDots = document.querySelectorAll('#alloy-slideshow-dots .dot');
    let currentAlloySlide = 0;
    const alloyInterval = 4000;

    const showAlloySlide = (index) => {
      if (index >= alloySlides.length) index = 0;
      currentAlloySlide = index;

      alloySlides.forEach((slide, i) => {
        if (i === currentAlloySlide) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      alloyDots.forEach((dot, i) => {
        if (i === currentAlloySlide) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });
    };

    alloyDots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        showAlloySlide(index);
      });
    });

    if (alloySlides.length > 0) {
      setInterval(() => {
        showAlloySlide(currentAlloySlide + 1);
      }, alloyInterval);
    }
  };

  initAlloySlideshow();


  /* ==========================================================================
     6. SEE MORE IMAGES GRID ENGINE (alloy.html ONLY)
     ========================================================================== */
  const initSeeMoreButton = () => {
    const seeMoreBtn = document.getElementById('see-more-btn');
    if (!seeMoreBtn) return; // Clean exit if not on alloy.html

    const hiddenItems = document.querySelectorAll('.gallery-grid-20 .gallery-item.hidden-item');
    const btnWrapper = seeMoreBtn.parentElement;

    seeMoreBtn.addEventListener('click', () => {
      hiddenItems.forEach(item => {
        item.classList.remove('hidden-item');
        // Let it fade or scale nicely via CSS
        item.style.opacity = '0';
        item.offsetHeight; // trigger reflow
        item.style.transition = 'opacity 0.6s cubic-bezier(0.25, 0.8, 0.25, 1)';
        item.style.opacity = '1';
      });

      // Hide button cleanly
      btnWrapper.style.display = 'none';

      // Re-trigger Lightbox mapping to capture newly revealed 8 images!
      initLightboxForGrid('alloy-gallery-grid-scope');
    });
  };

  initSeeMoreButton();


  /* ==========================================================================
     7. PROJECTS CARD CAROUSELS MODULE (projects.html ONLY)
     ========================================================================== */
  const initProjectSliders = () => {
    const projectCards = document.querySelectorAll('.project-slide-card');
    if (projectCards.length === 0) return; // Clean exit if not on projects.html

    const projectInterval = 2500;

    projectCards.forEach((card, cardIdx) => {
      const slides = card.querySelectorAll('.proj-slide');
      const dots = card.querySelectorAll('.mini-dot');
      let currentProjSlideIdx = 0;
      let timer = null;

      const showProjSlide = (idx) => {
        if (idx >= slides.length) idx = 0;
        currentProjSlideIdx = idx;

        slides.forEach((slide, i) => {
          if (i === currentProjSlideIdx) {
            slide.classList.add('active');
          } else {
            slide.classList.remove('active');
          }
        });

        dots.forEach((dot, i) => {
          if (i === currentProjSlideIdx) {
            dot.classList.add('active');
          } else {
            dot.classList.remove('active');
          }
        });
      };

      // Stagger rotation triggers to keep renders super-smooth
      setTimeout(() => {
        timer = setInterval(() => {
          showProjSlide(currentProjSlideIdx + 1);
        }, projectInterval);
      }, cardIdx * 150);

      // Pause slide loops on hover
      card.addEventListener('mouseenter', () => {
        if (timer) clearInterval(timer);
      });

      card.addEventListener('mouseleave', () => {
        timer = setInterval(() => {
          showProjSlide(currentProjSlideIdx + 1);
        }, projectInterval);
      });
    });
  };

  initProjectSliders();


  /* ==========================================================================
     8. DYNAMIC LIGHTBOX MODAL (alloy.html & furniture.html)
     ========================================================================== */
  const lightbox = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-main-img');
  const lightboxTitle = document.getElementById('lightbox-image-title');
  const lightboxCounter = document.getElementById('lightbox-image-counter');
  const lightboxLoader = document.getElementById('lightbox-loader');
  
  const closeBtn = document.getElementById('lightbox-close-btn');
  const prevImgBtn = document.getElementById('lightbox-prev-btn');
  const nextImgBtn = document.getElementById('lightbox-next-btn');
  const playSlideshowBtn = document.getElementById('lightbox-play-btn');

  let activeGalleryItems = [];
  let currentActiveIndex = 0;
  let isPlaySlideshow = false;
  let playTimer = null;

  // Coded with global scoop wrapper to bind files dynamically
  window.initLightboxForGrid = (gridClassOrId) => {
    const container = document.querySelector(`.${gridClassOrId}`) || document.getElementById(gridClassOrId);
    if (!container) return;

    // Filter only visible active items (skips .hidden-item in alloy grid)
    const getActiveItems = () => {
      return Array.from(container.querySelectorAll('.gallery-item')).filter(item => {
        return window.getComputedStyle(item).display !== 'none';
      });
    };

    const attachClickEvents = () => {
      const currentVisibleItems = getActiveItems();
      currentVisibleItems.forEach((item, index) => {
        // Clone nodes or remove old listener to prevent multiple clicks
        const newBtn = item.cloneNode(true);
        item.parentNode.replaceChild(newBtn, item);

        newBtn.addEventListener('click', function(e) {
          e.preventDefault();
          // Pool dynamic scoped items
          activeGalleryItems = getActiveItems();
          currentActiveIndex = activeGalleryItems.indexOf(newBtn);
          if (currentActiveIndex === -1) currentActiveIndex = index;
          openLightbox();
        });
      });
    };

    attachClickEvents();
  };

  const openLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
    loadLightboxImage();
  };

  const closeLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    stopLightboxPlay();
  };

  const loadLightboxImage = () => {
    if (activeGalleryItems.length === 0 || !lightboxImg) return;
    
    if (lightboxLoader) lightboxLoader.style.display = 'block';
    
    const activeItem = activeGalleryItems[currentActiveIndex];
    const imageSrc = activeItem.getAttribute('data-src');
    const titleSpan = activeItem.querySelector('.gallery-item-title');
    const imageTitle = titleSpan ? titleSpan.textContent : 'Modular Systems';

    const imgObj = new Image();
    imgObj.src = imageSrc;
    imgObj.onload = () => {
      lightboxImg.src = imageSrc;
      if (lightboxTitle) lightboxTitle.textContent = imageTitle;
      if (lightboxCounter) lightboxCounter.textContent = `${currentActiveIndex + 1} / ${activeGalleryItems.length}`;
      if (lightboxLoader) lightboxLoader.style.display = 'none';
    };
    imgObj.onerror = () => {
      lightboxImg.src = imageSrc;
      if (lightboxTitle) lightboxTitle.textContent = imageTitle;
      if (lightboxCounter) lightboxCounter.textContent = `${currentActiveIndex + 1} / ${activeGalleryItems.length}`;
      if (lightboxLoader) lightboxLoader.style.display = 'none';
    };
  };

  const nextLightboxImage = () => {
    currentActiveIndex = (currentActiveIndex + 1) % activeGalleryItems.length;
    loadLightboxImage();
  };

  const prevLightboxImage = () => {
    currentActiveIndex = (currentActiveIndex - 1 + activeGalleryItems.length) % activeGalleryItems.length;
    loadLightboxImage();
  };

  const toggleLightboxPlay = () => {
    if (isPlaySlideshow) {
      stopLightboxPlay();
    } else {
      isPlaySlideshow = true;
      if (playSlideshowBtn) {
        playSlideshowBtn.textContent = '⏸ Pause';
        playSlideshowBtn.style.backgroundColor = 'var(--green)';
      }
      playTimer = setInterval(nextLightboxImage, 3000);
    }
  };

  const stopLightboxPlay = () => {
    isPlaySlideshow = false;
    if (playSlideshowBtn) {
      playSlideshowBtn.textContent = '▶ Play';
      playSlideshowBtn.style.backgroundColor = '';
    }
    if (playTimer) clearInterval(playTimer);
  };

  // Bind clicks
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-content-frame')) {
        closeLightbox();
      }
    });
  }

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  
  if (nextImgBtn) {
    nextImgBtn.addEventListener('click', () => {
      nextLightboxImage();
      stopLightboxPlay();
    });
  }
  
  if (prevImgBtn) {
    prevImgBtn.addEventListener('click', () => {
      prevLightboxImage();
      stopLightboxPlay();
    });
  }
  
  if (playSlideshowBtn) playSlideshowBtn.addEventListener('click', toggleLightboxPlay);

  document.addEventListener('keydown', (e) => {
    if (!lightbox || !lightbox.classList.contains('active')) return;
    
    if (e.key === 'Escape') {
      closeLightbox();
    } else if (e.key === 'ArrowRight') {
      nextLightboxImage();
      stopLightboxPlay();
    } else if (e.key === 'ArrowLeft') {
      prevLightboxImage();
      stopLightboxPlay();
    }
  });

  // Initialize lightbox on grids (if present on active page)
  initLightboxForGrid('gallery-grid-20');
  initLightboxForGrid('gallery-grid-8');


  /* ==========================================================================
     9. CONTACT FORM CALCULATION VALIDATION (contact.html & PREVIEWS)
     ========================================================================== */
  const initContactForm = () => {
    const contactForm = document.getElementById('ecospace-contact-form');
    if (!contactForm) return; // Clean exit if not present

    const successOverlay = document.getElementById('contact-success-box');
    const closeSuccessBtn = document.getElementById('btn-close-success');
    const submitBtn = document.getElementById('btn-submit-form');

    const nameInput = document.getElementById('contact-name');
    const emailInput = document.getElementById('contact-email');
    const messageInput = document.getElementById('contact-message');

    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    const validateInput = (input, groupSelector, errorClass, customCheck = () => true) => {
      const group = input.closest(groupSelector);
      if (!input.value.trim() || !customCheck(input.value.trim())) {
        group.classList.add(errorClass);
        return false;
      } else {
        group.classList.remove(errorClass);
        return true;
      }
    };

    if (nameInput) nameInput.addEventListener('input', () => nameInput.closest('.input-group').classList.remove('invalid-field'));
    if (emailInput) emailInput.addEventListener('input', () => emailInput.closest('.input-group').classList.remove('invalid-field'));
    if (messageInput) messageInput.addEventListener('input', () => messageInput.closest('.input-group').classList.remove('invalid-field'));

    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      const isNameValid = validateInput(nameInput, '.input-group', 'invalid-field');
      const isEmailValid = validateInput(emailInput, '.input-group', 'invalid-field', (val) => emailRegex.test(val));
      const isMessageValid = validateInput(messageInput, '.input-group', 'invalid-field');

      if (isNameValid && isEmailValid && isMessageValid) {
        submitBtn.classList.add('submitting');
        submitBtn.disabled = true;

        /* ==========================================================================
           WEB3FORMS HOOKUP INTEGRATION:
           To activate backend mailings, uncomment standard fetch pipeline:
           
           const formData = new FormData(contactForm);
           formData.append("access_key", "YOUR_ACCESS_KEY_HERE");
           
           fetch("https://api.web3forms.com/submit", {
             method: "POST",
             body: formData
           })
           .then(async (response) => {
              if (response.status == 200) {
                 showSuccessState();
              } else {
                 alert("Inquiry failed to send. Check connections.");
              }
           })
           .catch(() => alert("Connection error."))
           .finally(() => {
              submitBtn.classList.remove('submitting');
              submitBtn.disabled = false;
           });
           ========================================================================== */

        // Simulating standard validation checks delays
        setTimeout(() => {
          showSuccessState();
        }, 1500);
      }
    });

    const showSuccessState = () => {
      if (successOverlay) successOverlay.classList.add('active');
      submitBtn.classList.remove('submitting');
      submitBtn.disabled = false;
    };

    if (closeSuccessBtn) {
      closeSuccessBtn.addEventListener('click', () => {
        if (successOverlay) successOverlay.classList.remove('active');
        contactForm.reset();
        
        const inputs = contactForm.querySelectorAll('.floating-input');
        inputs.forEach(input => {
          input.closest('.input-group').classList.remove('invalid-field');
        });
      });
    }
  };

  initContactForm();

});
