// home section image changes

let home = document.getElementById('home');

let source_image = ['/static/assets/css/bg/1.jpg', '/static/assets/css/bg/2.jpg', '/static/assets/css/bg/3.jpg'];

let _title = ["O'zbek madaniy merosi", "O'zbek me'morchiligi", "Xalq san'ati"];
let _subtitle = [
    "O‘zbekiston madaniyati, Markaziy Osiyo xalqlarining ko‘p asrlik an’analari va turmush tarzi bilan chambarchas bog‘liq boy tarixga ega",
    "Me’morchilik ijodining gullab-yashnashi O‘zbekiston Buyuk Ipak yo‘lining markazi bo‘lgan o‘rta asrlar davriga to‘g‘ri keladi. XIV asrdan boshlab bu yerda dunyoga mashhur me’morchilik yodgorliklari – Samarqanddagi Registon maydoni, Shohi-Zinda majmuasi, Bibixonim masjidi va Gur-Amir maqbarasi, Shahrisabzdagi Oqsaroy, Buxorodagi Poyi kalon va Labi Hovuz, Xivada minora va madrasalar barpo etildi.",
    "O‘zbekistonda azaldan noyob iste’dodli odamlar yashab, xalq san’atining  nodir an’analarini asrab-avaylab, avloddan-avlodga yetkazib kelmoqdalar. Ushbu an’analar bizning tariximizni, ajoyib madaniyatimiz va milliy qadriyatlarimizni unutishga yo‘l bermaydi.",
];

// setInterval(() => {
//     let random_image = source_image[Math.floor(Math.random() * source_image.length)]
//     setTimeout(() => {
//         home.style = `background-image: url(${random_image}) !important;`;
//     }, 1000)
// }, 3000);

// change text content

let text = document.querySelectorAll('.text-content');

let index = 0;

setInterval(() => {
    index++;
    if (index == text.length) {
        index = 0
    };
    changeTextContent(index)
}, 4000)

function changeTextContent(indexOfText) {
    text.forEach(e => {
        e.style.display = 'none';
    });
    home.style = `background-image: url(${source_image[index]}) !important;`;
    text[indexOfText].style.display = 'block';
}

function scrollTrigger() {
    let navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 133) {
            navbar.classList.add('scroll');
        } else {
            navbar.classList.remove('scroll');
        }
    })
}

function openModal() {
    document.querySelector('.modal').classList.add('is-active');
}

function closeModal() {
    document.querySelector('.modal').classList.remove('is-active');
}

document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {

            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');

        });
    });

});


scrollTrigger();

let _content = document.createElement('div');

function openImage(src) {
    _content.innerHTML = `
        <div class="modal is-active">
            <div class="modal-background"></div>
            <div class="modal-content">
                <figure class="image is-4by3">
                    <img src="${src}" alt="">
                </figure>
            </div>
            <button class="modal-close is-large" aria-label="close" onclick="remove()"></button>
        </div>
    `
    document.body.appendChild(_content)
}

function remove() {
    document.body.removeChild(_content)
}

var swiper = new Swiper(".mySwiper", {
    scrollbar: {
        el: ".swiper-scrollbar",
        hide: true,
    },
    autoplay: {
        delay: 3000,
    },
    slidesPerView: 2,
    slidesPerMove: 1,
    loop: true,

    breakpoints: {
        // when window width is >= 320px
        220: {
          slidesPerView: 1,
          spaceBetween: 20
        },
        // when window width is >= 480px
        768: {
          slidesPerView: 2,
          spaceBetween: 30
        },
        // when window width is >= 640px
        1920: {
          slidesPerView: 3,
          spaceBetween: 40
        }
      }
  });

  window.addEventListener("resize", () => {
      if (window.innerWidth > 1920) {
          document.querySelectorAll('.container-widescreen').forEach(e=>{
              e.classList.add('container');
          })
          document.querySelectorAll('.has-text-centered-mobile').forEach(t => {
              t.classList.add('has-text-centered')
          })
      }
      else {
        document.querySelectorAll('.container-widescreen').forEach(e=>{
            e.classList.remove('container');
        })
        document.querySelectorAll('.has-text-centered-mobile').forEach(t => {
            t.classList.remove('has-text-centered')
        })
      }
  })