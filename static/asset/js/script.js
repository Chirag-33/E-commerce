// const headerImage = document.querySelector('.content img');

// function changeImage() {
//   const imagePaths = [
   
//     'static/asset/images/header2.jpg',
//     'static/asset/images/header3.jpg',
//     'static/asset/images/header4.jpg',
//     'static/asset/images/header5.jpg'
   
//   ];
//   let imageIndex = 0;

//   function changeImageSrc() {
//     const imagePath = imagePaths[imageIndex];
//     headerImage.src = imagePath; 
//     imageIndex = (imageIndex + 1) % imagePaths.length;
//   }

//   setInterval(changeImageSrc, 3000); 
// }

// changeImage();
  



// -------------------------------------arrow---------------------------------------------------------



document.addEventListener('DOMContentLoaded', () => {
    const leftArrows = document.getElementsByClassName('left-arrow');
    const rightArrows = document.getElementsByClassName('right-arrow');
    const productContainers = document.getElementsByClassName('product-container');
    
    const productCardWidth = 300; // Or use .offsetWidth to get dynamic size

    for (let i = 0; i < productContainers.length; i++) {
        let currentIndex = 0;
        const container = productContainers[i];
        const leftArrow = leftArrows[i];
        const rightArrow = rightArrows[i];

        leftArrow.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                container.scrollBy({
                    left: -productCardWidth,
                    behavior: 'smooth'
                });
            }
        });

        rightArrow.addEventListener('click', () => {
            const visibleProducts = Math.floor(container.clientWidth / productCardWidth);
            const totalProducts = container.children.length;

            if (currentIndex < totalProducts - visibleProducts) {
                currentIndex++;
                container.scrollBy({
                    left: productCardWidth,
                    behavior: 'smooth'
                });
            }
        });
    }
});


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






// ----------------------------------------------User Profile-----------------------------------------------------------
document.addEventListener('DOMContentLoaded',()=>{
    const profile_image = document.getElementById('user-icon')
    const profile_dropDown = document.getElementById('profile_dropDown')

    profile_image.addEventListener('click',()=>{
        if (profile_dropDown.style.display === 'none' || profile_dropDown.style.display==''){
            profile_dropDown.style.display='block'
        }else{
            profile_dropDown.style.display = 'none'
        }
        
        document.addEventListener('click',(event)=>{
            if(!profile_image.contains(event.target)&& !profile_dropDown.contains(event.target)){
                profile_dropDown.style.display = 'none'
            }
            
        })
    })
})