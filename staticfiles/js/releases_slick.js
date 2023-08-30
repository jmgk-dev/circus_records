$('.artist_list').slick({
    dots: true,
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
        }
      },

      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
        }
      },

      {
        breakpoint: 900,
        settings: {
          slidesToShow: 2.5,
          slidesToScroll: 2,
        }
      },

      {
        breakpoint: 750,
        settings: {
          slidesToShow: 2.13,
          slidesToScroll: 2,
        }
      },

      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1.5,
          slidesToScroll: 2,
        }
      },
      
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1.13,
          slidesToScroll: 1,
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });