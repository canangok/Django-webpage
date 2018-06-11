(function($){
    'use strict';

    //menu options
    var fixed_top = $(".main-menu");
    var fixed_top_two = $(".menu-two");
    var fixed_top_four = $(".menu-four");
    var fixed_top_five = $(".menu-five");
    var fixed_top_six = $(".menu-six");

    $(window).on('scroll', function(){

      if( $(this).scrollTop() > 100 ){
        fixed_top.addClass("animated fadeInDown");
      }
      else{
        fixed_top.removeClass("animated fadeInDown");
      }

	  if( $(this).scrollTop() > 100 ){
        fixed_top_two.addClass("menu-two-bg");
      }
      else{
        fixed_top_two.removeClass("menu-two-bg");
      }

	  if( $(this).scrollTop() > 100 ){
        fixed_top_four.addClass("menu-four-bg");
      }
      else{
        fixed_top_four.removeClass("menu-four-bg");
      }

    if( $(this).scrollTop() > 100 ){
        fixed_top_five.addClass("menu-five-bg");
      }
      else{
        fixed_top_five.removeClass("menu-five-bg");
      }

    if( $(this).scrollTop() > 100 ){
        fixed_top_six.addClass("menu-six-bg");
      }
      else{
        fixed_top_six.removeClass("menu-six-bg");
      }

    });

  //jQuery for page scrolling feature - requires jQuery Easing plugin
    /*$('ul.nav').each( function( i, liList ) {
      var $liList = $( liList );
      $liList.on( 'click', 'li a', function(event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');
      event.preventDefault();
      });
    });*/


	//counter up
    $('.counter').each(function() {
      var $this = $(this),
        countTo = $this.attr('data-count');

      $({ countNum: $this.text()}).animate({
        countNum: countTo
      },

      {
        duration: 2000,
        /*easing:'linear',*/
        step: function() {
          $this.text(Math.floor(this.countNum));
        },
        complete: function() {
          $this.text(this.countNum);
          //alert('finished');
        }

      });

  });


	//Product list grid view
	var list = $("#list");
	var grid = $("#grid");
	/*list.on('click', function(){
	  $('.product-item-grid').animate({opacity:0},function(){
		  $('.grid').removeClass('grid-active');
		  $('.list').addClass('list-active');
		  $('.product-item-grid').attr('class', 'product-item-list shadow');
		  $('.product-item-list').stop().animate({opacity:1});
	  });
	});

	grid.on('click', function(){
	  $('.product-item-list').animate({opacity:0},function(){
		  $('.list').removeClass('list-active');
		  $('.grid').addClass('grid-active');
		  $('.product-item-list').attr('class', 'product-item-grid shadow');
		  $('.product-item-grid').stop().animate({opacity:1});
	  });
	});*/



  //lightcase
  $('a[data-rel^=lightcase]').lightcase();

  //directional-hover
  $(window).load(function() {
    $('.dh-container').directionalHover();
  });


  //masonery
  $('.grid').masonry({
    // set itemSelector so .grid-sizer is not used in layout
    itemSelector: '.grid-item',
    // use element for option
    columnWidth: '.grid-sizer',
    percentPosition: true
  })



  //Sponsor one
  var swiper = new Swiper('.sponsor-slider-one', {
      slidesPerView: 3,
      spaceBetween: 30,
      autoplay: 2000,
      loop: true,
      breakpoints: {
        // when window width is <= 320px
        320: {
          slidesPerView: 1
        },
        // when window width is <= 480px
        480: {
          slidesPerView: 2
        }
      }
    });

  //Sponsor two
  var swiper = new Swiper('.sponsor-slider-two', {
      slidesPerView: 4,
      spaceBetween: 15,
      autoplay: 1500,
      loop: true,
      breakpoints: {
        // when window width is <= 320px
        320: {
          slidesPerView: 1
        },
        // when window width is <= 480px
        480: {
          slidesPerView: 2
        },
        // when window width is <= 767px
        767: {
          slidesPerView: 3
        }
      }
    });

  //Sponsor Three
  var swiper = new Swiper('.sponsor-slider-three', {
      slidesPerView: 5,
      spaceBetween: 15,
      autoplay: 1000,
      loop: true,
      breakpoints: {
        // when window width is <= 320px
        320: {
          slidesPerView: 1
        },
        // when window width is <= 480px
        480: {
          slidesPerView: 2
        },
        // when window width is <= 767px
        767: {
          slidesPerView: 4
        }
      }
    });

})(jQuery);
