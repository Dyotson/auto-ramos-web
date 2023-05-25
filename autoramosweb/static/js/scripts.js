/*!
* Start Bootstrap - Stylish Portfolio v6.0.5 (https://startbootstrap.com/theme/stylish-portfolio***REMOVED***
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-stylish-portfolio/blob/master/LICENSE***REMOVED***
*/
window.addEventListener('DOMContentLoaded', event => {

    const sidebarWrapper = document.getElementById('sidebar-wrapper'***REMOVED***;
    let scrollToTopVisible = false;
    // Closes the sidebar menu
    const menuToggle = document.body.querySelector('.menu-toggle'***REMOVED***;
    menuToggle.addEventListener('click', event => {
        event.preventDefault(***REMOVED***;
        sidebarWrapper.classList.toggle('active'***REMOVED***;
        _toggleMenuIcon(***REMOVED***;
        menuToggle.classList.toggle('active'***REMOVED***;
***REMOVED***

    // Closes responsive menu when a scroll trigger link is clicked
    var scrollTriggerList = [***REMOVED***.slice.call(document.querySelectorAll('#sidebar-wrapper .js-scroll-trigger'***REMOVED***;
    scrollTriggerList.map(scrollTrigger => {
        scrollTrigger.addEventListener('click', (***REMOVED*** => {
            sidebarWrapper.classList.remove('active'***REMOVED***;
            menuToggle.classList.remove('active'***REMOVED***;
            _toggleMenuIcon(***REMOVED***;
    ***REMOVED***
***REMOVED***;

    function _toggleMenuIcon(***REMOVED*** {
        const menuToggleBars = document.body.querySelector('.menu-toggle > .fa-bars'***REMOVED***;
        const menuToggleTimes = document.body.querySelector('.menu-toggle > .fa-xmark'***REMOVED***;
        if (menuToggleBars***REMOVED*** {
            menuToggleBars.classList.remove('fa-bars'***REMOVED***;
            menuToggleBars.classList.add('fa-xmark'***REMOVED***;
    ***REMOVED***
        if (menuToggleTimes***REMOVED*** {
            menuToggleTimes.classList.remove('fa-xmark'***REMOVED***;
            menuToggleTimes.classList.add('fa-bars'***REMOVED***;
    ***REMOVED***
***REMOVED***

    // Scroll to top button appear
    document.addEventListener('scroll', (***REMOVED*** => {
        const scrollToTop = document.body.querySelector('.scroll-to-top'***REMOVED***;
        if (document.documentElement.scrollTop > 100***REMOVED*** {
            if (!scrollToTopVisible***REMOVED*** {
                fadeIn(scrollToTop***REMOVED***;
                scrollToTopVisible = true;
        ***REMOVED***
    ***REMOVED*** else {
            if (scrollToTopVisible***REMOVED*** {
                fadeOut(scrollToTop***REMOVED***;
                scrollToTopVisible = false;
        ***REMOVED***
    ***REMOVED***
***REMOVED***
***REMOVED***

function fadeOut(el***REMOVED*** {
    el.style.opacity = 1;
    (function fade(***REMOVED*** {
        if ((el.style.opacity -= .1***REMOVED*** < 0***REMOVED*** {
            el.style.display = "none";
    ***REMOVED*** else {
            requestAnimationFrame(fade***REMOVED***;
    ***REMOVED***
***REMOVED***(***REMOVED***;
***REMOVED***;

function fadeIn(el, display***REMOVED*** {
    el.style.opacity = 0;
    el.style.display = display || "block";
    (function fade(***REMOVED*** {
        var val = parseFloat(el.style.opacity***REMOVED***;
        if (!((val += .1***REMOVED*** > 1***REMOVED*** {
            el.style.opacity = val;
            requestAnimationFrame(fade***REMOVED***;
    ***REMOVED***
***REMOVED***(***REMOVED***;
***REMOVED***;
