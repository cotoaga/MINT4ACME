/**
 * Simple slideshow script to replace the original Java applet
 * This mimics the behavior of the 1997 Java slideshow that cycled through images
 */

class Slideshow {
    constructor(elementId, images, interval = 3000) {
        this.container = document.getElementById(elementId);
        if (!this.container) {
            console.error(`Element with ID "${elementId}" not found.`);
            return;
        }
        
        this.images = images;
        this.interval = interval;
        this.currentIndex = 0;
        this.timer = null;
        this.isPlaying = false;
        
        // Create elements
        this.initializeDOM();
        
        // Start slideshow
        this.start();
        
        // Set up event listeners
        this.setupEventListeners();
    }
    
    initializeDOM() {
        // Create slideshow container
        this.slideshowContainer = document.createElement('div');
        this.slideshowContainer.className = 'slideshow-container';
        
        // Create image element
        this.imageElement = document.createElement('img');
        this.imageElement.className = 'slideshow-image';
        this.imageElement.alt = 'Slideshow Image';
        this.imageElement.src = this.images[0];
        
        // Create controls
        this.controls = document.createElement('div');
        this.controls.className = 'slideshow-controls';
        
        // Play/Pause button
        this.playPauseBtn = document.createElement('button');
        this.playPauseBtn.className = 'slideshow-btn';
        this.playPauseBtn.innerHTML = '⏸️'; // Pause symbol
        
        // Previous button
        this.prevBtn = document.createElement('button');
        this.prevBtn.className = 'slideshow-btn';
        this.prevBtn.innerHTML = '⏮️'; // Previous symbol
        
        // Next button
        this.nextBtn = document.createElement('button');
        this.nextBtn.className = 'slideshow-btn';
        this.nextBtn.innerHTML = '⏭️'; // Next symbol
        
        // Counter
        this.counter = document.createElement('span');
        this.counter.className = 'slideshow-counter';
        this.updateCounter();
        
        // Caption
        this.caption = document.createElement('div');
        this.caption.className = 'slideshow-caption';
        this.caption.textContent = 'Java applet slideshow - Vehicle configuration simulation';
        
        // Assemble the DOM structure
        this.controls.appendChild(this.prevBtn);
        this.controls.appendChild(this.playPauseBtn);
        this.controls.appendChild(this.nextBtn);
        this.controls.appendChild(this.counter);
        
        this.slideshowContainer.appendChild(this.imageElement);
        this.slideshowContainer.appendChild(this.controls);
        this.slideshowContainer.appendChild(this.caption);
        
        this.container.innerHTML = ''; // Clear container
        this.container.appendChild(this.slideshowContainer);
    }
    
    setupEventListeners() {
        this.playPauseBtn.addEventListener('click', () => this.togglePlayPause());
        this.prevBtn.addEventListener('click', () => this.showPrevious());
        this.nextBtn.addEventListener('click', () => this.showNext());
        
        // Add hover event - original Java applets often paused when mouse was over them
        this.slideshowContainer.addEventListener('mouseenter', () => {
            if (this.isPlaying) {
                this.pause();
                this.wasPlayingBeforeHover = true;
            }
        });
        
        this.slideshowContainer.addEventListener('mouseleave', () => {
            if (this.wasPlayingBeforeHover) {
                this.start();
                this.wasPlayingBeforeHover = false;
            }
        });
    }
    
    updateCounter() {
        this.counter.textContent = `${this.currentIndex + 1}/${this.images.length}`;
    }
    
    showImage(index) {
        // Ensure index is within bounds
        if (index < 0) {
            index = this.images.length - 1;
        } else if (index >= this.images.length) {
            index = 0;
        }
        
        this.currentIndex = index;
        this.imageElement.src = this.images[this.currentIndex];
        this.updateCounter();
    }
    
    showNext() {
        this.showImage(this.currentIndex + 1);
    }
    
    showPrevious() {
        this.showImage(this.currentIndex - 1);
    }
    
    start() {
        if (!this.isPlaying) {
            this.isPlaying = true;
            this.playPauseBtn.innerHTML = '⏸️'; // Pause symbol
            this.timer = setInterval(() => this.showNext(), this.interval);
        }
    }
    
    pause() {
        if (this.isPlaying) {
            this.isPlaying = false;
            this.playPauseBtn.innerHTML = '▶️'; // Play symbol
            clearInterval(this.timer);
        }
    }
    
    togglePlayPause() {
        if (this.isPlaying) {
            this.pause();
        } else {
            this.start();
        }
    }
}

// Initialize all slideshows when the document is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if we have the slideshow container
    const slideshowContainer = document.getElementById('java-slideshow');
    if (slideshowContainer) {
        // Create array of image paths from 4_8pic1.jpg to 4_8pic9.jpg
        const images = [];
        for (let i = 1; i <= 9; i++) {
            images.push(`../original/objects/4_8pic${i}.jpg`);
        }
        
        // Initialize slideshow
        new Slideshow('java-slideshow', images, 3000);
    }
});

// Add CSS to the document
const style = document.createElement('style');
style.textContent = `
.slideshow-container {
    position: relative;
    max-width: 100%;
    margin: 0 auto;
    overflow: hidden;
    border: 2px solid #666;
    background-color: #f0f0f0;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.slideshow-image {
    display: block;
    width: 100%;
    max-height: 400px;
    object-fit: contain;
}

.slideshow-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    background-color: #e0e0e0;
    border-top: 1px solid #ccc;
}

.slideshow-btn {
    background-color: #f8f8f8;
    border: 1px solid #999;
    border-radius: 3px;
    margin: 0 5px;
    padding: 5px 10px;
    cursor: pointer;
    font-size: 14px;
}

.slideshow-btn:hover {
    background-color: #ddd;
}

.slideshow-counter {
    margin-left: 15px;
    font-family: monospace;
    color: #666;
}

.slideshow-caption {
    padding: 10px;
    text-align: center;
    font-style: italic;
    background-color: #e8e8e8;
    border-top: 1px solid #ccc;
    color: #333;
}

/* Vintage styling to make it look more like a Java applet from 1997 */
.java-applet-style {
    font-family: 'Courier New', monospace;
    padding: 5px;
    background-color: #e6e6e6;
    color: #333;
    font-size: 10px;
    text-align: center;
    border-top: 1px solid #ccc;
}
`;
document.head.appendChild(style);