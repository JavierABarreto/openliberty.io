/*******************************************************************************
 * Copyright (c) 2017 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     IBM Corporation - initial API and implementation
 *******************************************************************************/

var latest_release_url = '/api/builds/latest';

$(document).ready(function() {
    // add custom css to twitter iframe
    $('#twitter_iframe_div').on('DOMSubtreeModified propertychange',"#twitter-widget-0", function() {
        $(".twitter-timeline").contents().find(".timeline-Tweet-media").css("display", "none");
        $(".twitter-timeline").contents().find(".timeline-Tweet-text").css({"font-size": "16px", "margin-bottom": "-10px"});
        $(".twitter-timeline").contents().find(".timeline-Body").css("border-bottom", "none");
    });

});


document.addEventListener("DOMContentLoaded", function() {
    const imageObserver = new IntersectionObserver(function(entries, imgObserver) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const lazyImage = entry.target;
                lazyImage.src = lazyImage.dataset.src;
                lazyImage.classList.remove("lazy");
                imgObserver.unobserve(lazyImage);
            }
        });
    });
    const arr = document.querySelectorAll('img.lazy');
    arr.forEach(function(v) {
        imageObserver.observe(v);
    });
})
