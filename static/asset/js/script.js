const headerImage = document.querySelector('.hero-section .content img');

function changeImage() {
  const imagePaths = [
    'static/asset/images/header.jpg',
    'static/asset/images/header2.jpg',
    'static/asset/images/header3.jpg'
   
  ];
  let imageIndex = 0;

  function changeImageSrc() {
    const imagePath = imagePaths[imageIndex];
    headerImage.src = imagePath; 
    imageIndex = (imageIndex + 1) % imagePaths.length;
  }

  setInterval(changeImageSrc, 2000); 
}

changeImage();
  


const createFooter = () => {
    let footer = document.querySelector('footer');
    let logoUrl = footer.getAttribute('data-logo-url');
    
    footer.innerHTML = `
    <div class="footer-content">
        <img src="${logoUrl}" class="logo" alt="">
        <div class="footer-ul-container">
            <ul class="category">
                <li class="category-title">men</li>
                <li><a href="#" class="footer-link">t-shirts</a></li>
                <li><a href="#" class="footer-link">sweatshirts</a></li>
                <li><a href="#" class="footer-link">shirts</a></li>
                <li><a href="#" class="footer-link">jeans</a></li>
                <li><a href="#" class="footer-link">trousers</a></li>
                <li><a href="#" class="footer-link">shoes</a></li>
                <li><a href="#" class="footer-link">formals</a></li>
                <li><a href="#" class="footer-link">sports</a></li>
                <li><a href="#" class="footer-link">watch</a></li>
            </ul>
            <ul class="category">
                <li class="category-title">women</li>
                <li><a href="#" class="footer-link">t-shirts</a></li>
                <li><a href="#" class="footer-link">sweatshirts</a></li>
                <li><a href="#" class="footer-link">shirts</a></li>
                <li><a href="#" class="footer-link">jeans</a></li>
                <li><a href="#" class="footer-link">trousers</a></li>
                <li><a href="#" class="footer-link">shoes</a></li>
                <li><a href="#" class="footer-link">casuals</a></li>
                <li><a href="#" class="footer-link">formals</a></li>
                <li><a href="#" class="footer-link">sports</a></li>
                <li><a href="#" class="footer-link">watch</a></li>
            </ul>
        </div>
    </div>
    <p class="footer-title">about company</p>
    <p class="info">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repellat tempore ad suscipit, eos eius quisquam sed optio nisi quaerat fugiat ratione et vero maxime praesentium, architecto minima reiciendis iste quo deserunt assumenda alias ducimus. Ullam odit maxime id voluptates rerum tenetur corporis laboriosam! Cum error ipsum laborum tempore in rerum necessitatibus nostrum nobis modi! Debitis adipisci illum nemo aperiam sed, et accusamus ut officiis. Laborum illo exercitationem quo culpa reprehenderit excepturi distinctio tempore cupiditate praesentium nisi ut iusto, assumenda perferendis facilis voluptas autem fuga sunt ab debitis voluptatum harum eum. Asperiores, natus! Est deserunt incidunt quasi placeat omnis, itaque harum?</p>
    <p class="info">support emails - help@clothing.com, customersupport@clothing.com</p>
    <p class="info">telephone - 180 00 00 001, 180 00 00 002</p>
    <div class="footer-social-container">
        <div>
            <a href="#" class="social-link">terms & services</a>
            <a href="#" class="social-link">privacy page</a>
        </div>
        <div>
            <a href="#" class="social-link">instagram</a>
            <a href="#" class="social-link">facebook</a>
            <a href="#" class="social-link">twitter</a>
        </div>
    </div>
    <p class="footer-credit">Clothing, Best apparels online store</p>
    `;
}

createFooter();


const productImages = document.querySelectorAll(".product-images img"); 
const productImageSlide = document.querySelector(".image-slider"); 

let activeImageSlide = 0;

productImages.forEach((item, i) => { 
    item.addEventListener('click', () => { 
        productImages[activeImageSlide].classList.remove('active'); 
        item.classList.add('active'); 
        productImageSlide.style.backgroundImage = `url('${item.src}')`;
        activeImageSlide = i; 
    })
})


const sizeBtns = document.querySelectorAll('.size-radio-btn');
let checkedBtn = 0; 

sizeBtns.forEach((item, i) => { 
    item.addEventListener('click', () => { 
        sizeBtns[checkedBtn].classList.remove('check'); 
        item.classList.add('check'); 
        checkedBtn = i;
    })
})

document.addEventListener('DOMContentLoaded', function() { 
    var searchInput = document.getElementById('search-input');
    var suggestionsBox = document.getElementById('suggestions');

    // Hide suggestions when clicking outside
    document.addEventListener('click', function(e) {
        if (!suggestionsBox.contains(e.target) && e.target !== searchInput) {
            suggestionsBox.innerHTML = '';
        }
    });

    // Hide suggestions on pressing Esc key
    searchInput.addEventListener('keydown', function(e) {
        if (e.key === "Escape") {
            suggestionsBox.innerHTML = '';
        }
    });

    // Handle input for search and display suggestions
    searchInput.addEventListener('keyup', function() {
        var query = this.value;
        if (query.length > 1) {
            fetch(`/product-autocomplete/?q=${query}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    data.forEach(function(item) {
                        var div = document.createElement('div');
                        div.textContent = item;
                        div.classList.add('suggestion-item');

                        // Add click event to populate the input field and hide suggestions
                        div.addEventListener('click', function() {
                            searchInput.value = item; // Fill input field with clicked item
                            suggestionsBox.innerHTML = ''; // Clear suggestions
                        });

                        suggestionsBox.appendChild(div);
                    });
                })
                .catch(error => console.error('Fetch error:', error));
        } else {
            suggestionsBox.innerHTML = '';
        }
    });
});




// ----------------------------------------------User Profile-----------------------------------------------------------

document.addEventListener('DOMContentLoaded', (event)=>{
    const profileImage = document.getElementById('profile_image')
    const profileDropsown = document.getElementById('profiledropdown')

    profileImage.addEventListener('click', ()=>{
        if (profileDropsown.style.display==='none' || profileDropsown.style.display == ''){
            profileDropsown.style.display = 'block'
        }else{
            profileDropsown.style.display = 'none'
        }
        document.addEventListener('click', (event)=>{
            if (!profileImage.contains(event.target) && !profileDropsown.contains(event.target)){
                profileDropsown.style.display = 'none'
            }
        })
    })
})