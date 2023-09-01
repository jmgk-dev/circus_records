$('.slick_list').slick({
    dots: false,
    arrows: false,
    infinite: false,
    speed: 300,
    slidesToShow: 5,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1500,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 3,
          dots: true,
          arrows: true,
        }
      },

      {
        breakpoint: 1250,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          dots: true,
          arrows: true,
        }
      },

      {
        breakpoint: 1000,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          dots: true,
          arrows: true,
        }
      },

      {
        breakpoint: 750,
        settings: {
          slidesToShow: 2.13,
          slidesToScroll: 2,
          dots: true,
        }
      },

      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1.5,
          slidesToScroll: 2,
          dots: true,
        }
      },
      
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1.13,
          slidesToScroll: 1,
          dots: true,
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });