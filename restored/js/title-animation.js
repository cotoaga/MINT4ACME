/**
 * Title Animation - A modern replacement for the original Flash title animations
 * Simulates the experience of the 1997 Flash headers with CSS animations and JS
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize title animations 
    initTitleAnimations();
});

function initTitleAnimations() {
    // Find any title-text elements
    const titleElements = document.querySelectorAll('.title-text');
    
    titleElements.forEach(titleElement => {
        // Get the parent element
        const parentElement = titleElement.parentElement;
        const titleText = titleElement.textContent.trim();
        
        // Create the animated title container
        const animatedTitle = document.createElement('div');
        animatedTitle.className = 'animated-title';
        
        // Determine section from URL or text content
        const currentPath = window.location.pathname;
        const pathMatch = currentPath.match(/(\d+)_(\d+)\.html/);
        let section = '';
        
        if (pathMatch) {
            // Get section number from URL
            const sectionNum = parseInt(pathMatch[1]);
            
            switch(sectionNum) {
                case 1: section = 'introduction'; break;
                case 2: section = 'approach'; break;
                case 3: section = 'business'; break;
                case 4: section = 'technical'; break;
                case 5: section = 'project'; break;
                default: section = 'other';
            }
        } else {
            // Determine by title content
            const titleLower = titleText.toLowerCase();
            if (titleLower.includes('introduction')) section = 'introduction';
            else if (titleLower.includes('approach')) section = 'approach';
            else if (titleLower.includes('business')) section = 'business';
            else if (titleLower.includes('technical')) section = 'technical';
            else if (titleLower.includes('project')) section = 'project';
            else section = 'other';
        }
        
        animatedTitle.setAttribute('data-section', section);
        
        // Add icon based on section
        const icon = document.createElement('div');
        icon.className = 'title-icon';
        let iconSymbol = '🔗'; // Default link symbol
        
        switch(section) {
            case 'introduction': iconSymbol = '🔍'; break;
            case 'approach': iconSymbol = '🚗'; break;
            case 'business': iconSymbol = '💼'; break;
            case 'technical': iconSymbol = '⚙️'; break;
            case 'project': iconSymbol = '📊'; break;
        }
        
        icon.textContent = iconSymbol;
        
        // Try to find background image if available
        const sectionMatch = currentPath.match(/(\d+)_(\d+)\.html/);
        if (sectionMatch) {
            const bgImagePath = `../original/title/${sectionMatch[0].replace('.html', '.jpg')}`;
            
            // Create background image element
            const bgImage = document.createElement('img');
            bgImage.className = 'title-bg-image';
            bgImage.src = bgImagePath;
            bgImage.alt = '';
            bgImage.style.opacity = '0.6'; // 60% opacity - more visible background
            
            // Add the background image
            animatedTitle.appendChild(bgImage);
        }
        
        // Clone the title text element
        const newTitleText = titleElement.cloneNode(true);
        
        // Add elements to our animated container
        animatedTitle.appendChild(icon);
        animatedTitle.appendChild(newTitleText);
        
        // Replace the original title with our animated version
        parentElement.replaceChild(animatedTitle, titleElement);
    });
}

// Add some randomized subtle movement for more visual interest
function addRandomizedMovement() {
    const titles = document.querySelectorAll('.animated-title');
    
    titles.forEach(title => {
        // Subtle random rotation
        const rotation = (Math.random() * 0.5) - 0.25; // -0.25 to 0.25 degrees
        title.style.transform = `rotate(${rotation}deg)`;
        
        // Randomize animation delays slightly for natural feel
        const titleText = title.querySelector('.title-text');
        const icon = title.querySelector('.title-icon');
        
        if (titleText) {
            const delay = 0.3 + (Math.random() * 0.2); // 0.3 to 0.5 seconds
            titleText.style.animationDelay = `${delay}s`;
        }
        
        if (icon) {
            const delay = 0.2 + (Math.random() * 0.3); // 0.2 to 0.5 seconds
            icon.style.animationDelay = `${delay}s`;
        }
    });
}