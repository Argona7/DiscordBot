from .config import settings

browserSpoofingScript = """
            Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
            Object.defineProperty(navigator, 'vendor', { get: () => 'Google Inc.' });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => 16 });   

            const getImageData = HTMLCanvasElement.prototype.getContext;
            HTMLCanvasElement.prototype.ge
            tContext = function(type) {
                const context = getImageData.apply(this, arguments);
                if (type === '2d') {
                    const originalGetImageData = context.getImageData;
                    context.getImageData = function(...args) {
                        const data = originalGetImageData.apply(this, args);
                        for (let i = 0; i < data.data.length; i += 4) {
                            data.data[i] = data.data[i] ^ 0x80;
                        }
                        return data;
                    };
                }
                return context;
            };

            const getParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {
                if (parameter === 37445) return "MyBrand Inc.";  // GL_VENDOR
                if (parameter === 37446) return "MyBrand Graphics Engine";  // GL_RENDERER
                return getParameter.apply(this, arguments);
            };
                """

texts = [
    "Experience the magic of the blockchain with NFT Pixel Penguins, where each pixel tells a story.",
    "The NFT Pixel Penguins collection combines classic pixel art with cutting-edge technology for a unique experience.",
    "Join the thriving community of NFT Pixel Penguins and be part of an ever-growing digital family.",
    "With NFT Pixel Penguins, innovation meets artistry, creating digital assets that stand the test of time.",
    "NFT Pixel Penguins aren't just collectibles; they're an expression of creativity in the digital world.",
    "Discover the fusion of traditional pixel art and modern blockchain technology with NFT Pixel Penguins.",
    "Step into the vibrant world of NFT Pixel Penguins, where every penguin has a personality and a place in the metaverse.",
    "Each NFT Pixel Penguin is a masterpiece, combining nostalgic pixel design with futuristic potential.",
    "The charm of NFT Pixel Penguins lies in their simplicity, yet they hold immense value in the NFT market.",
    "Engage with the imaginative universe of NFT Pixel Penguins, where each creation is a testament to digital ingenuity.",
    "NFT Pixel Penguins bring together art and technology, creating timeless digital treasures.",
    "Dive into the world of NFT Pixel Penguins, where creativity knows no bounds and every penguin is a masterpiece.",
    "The vibrant designs of NFT Pixel Penguins breathe life into the blockchain, making each one a unique gem.",
    "NFT Pixel Penguins transform pixel art into digital gold, offering both beauty and blockchain utility.",
    "Celebrate the blend of nostalgia and innovation with NFT Pixel Penguins, each a digital marvel.",
    "NFT Pixel Penguins stand out in the NFT space, merging classic aesthetics with modern blockchain trends.",
    "Immerse yourself in the enchanting realm of NFT Pixel Penguins, where art and community thrive together.",
    "The beauty of NFT Pixel Penguins lies in their ability to turn simple pixels into powerful, valued assets.",
    "Each NFT Pixel Penguin carries a unique identity, bridging the gap between digital art and blockchain.",
    "NFT Pixel Penguins are more than collectibles; they're a movement that redefines digital creativity.",
    "Penguins on the blockchain offer a charming blend of creativity and digital innovation.",
    "Each penguin is a digital artwork, showcasing a perfect mix of nostalgia and modern flair.",
    "Dive into a world where pixelated penguins become timeless treasures on the blockchain.",
    "With each penguin, you're not just owning art but a piece of a vibrant digital ecosystem.",
    "These pixelated penguins stand out as icons of both simplicity and technological advancement.",
    "Join a community that celebrates the unique charm and value of every penguin in the collection.",
    "Penguins here are more than pixels; they are digital companions with a story to tell.",
    "Discover how pixel art penguins transform into prized assets in the ever-evolving NFT landscape.",
    "Step into a realm where every penguin holds a blend of creative expression and digital ownership.",
    "In the heart of this collection, penguins symbolize the future of art and community in the blockchain era.",
    "Explore a collection where every penguin tells a story through its pixelated charm and blockchain power.",
    "The charm of these penguins lies not only in their design but in the endless possibilities they bring to the digital world.",
    "Each penguin carries the spirit of creativity, transforming pixels into valuable assets in the NFT space.",
    "With every penguin, a new chapter in digital art unfolds, blending tradition with futuristic innovation.",
    "These penguins are a symbol of the digital era, where art and blockchain converge to create something truly unique.",
    "In this collection, penguins represent the perfect fusion of artistic expression and the boundless potential of the blockchain.",
    "Behind every penguin is a community that values creativity, innovation, and digital ownership.",
    "Penguins like these make a bold statement in the NFT world, offering both beauty and utility on the blockchain.",
    "Each penguin in the collection is a beacon of artistic vision, paving the way for new opportunities in the NFT market.",
    "Owning a penguin isn't just about the art; it's about becoming part of a larger movement in the world of NFTs and blockchain.",
    "LFG! Penguins are ready to conquer the blockchain.",
    "Catch the wave of creativity with penguins on the chain.",
    "Pixel penguins, endless possibilities.",
    "Get in early, the penguin party’s just begun!",
    "Owning a penguin means owning a piece of the future.",
    "Join the flock, be part of something big!",
    "The penguin revolution is here, don't miss out.",
    "Let’s go! Penguins are the next big thing in NFTs.",
    "Penguins on the blockchain — your next big move.",
    "Ready to mint your penguin? The time is now!",
    "Mint, hold, and let the penguins soar!",
    "Pixel perfection on the blockchain awaits.",
    "Join the penguin craze, it's just the beginning.",
    "Your next favorite NFT? A penguin, of course!",
    "The penguin parade is live, LFG!",
    "Every penguin minted, another story begins.",
    "From pixels to priceless — that's the penguin way.",
    "Penguins aren't just cool; they're the future of NFTs.",
    "Unlock the power of pixelated penguins today.",
    "The next big NFT? You guessed it, penguins!",
    "Pixel penguins, big rewards!",
    "Hop on the penguin train, LFG!",
    "Next-gen NFTs? Penguins lead the way.",
    "Ready, set, mint your penguin!",
    "Join the penguin movement today.",
    "Penguins rule the NFT world!",
    "Mint now, thank us later — penguins await!",
    "Dive into the penguin metaverse.",
    "Pixel penguins, limitless potential.",
    "Your penguin adventure starts now!",
    "Penguins to the moon! 🚀",
    "Pixel penguins are the new black.",
    "Own a penguin, own the future.",
    "Penguins are the new digital frontier.",
    "Flap into the future with penguins.",
    "Penguins: small pixels, big dreams.",
    "Mint a penguin, join the revolution.",
    "Pixelated penguins, infinite potential.",
    "Step into the penguin era, LFG!",
    "Penguins are more than NFTs; they’re a movement.",
    "Penguin power on the blockchain!",
    "Catch the penguin wave now!",
    "Tiny pixels, huge potential.",
    "Penguins leading the NFT charge!",
    "Every penguin, a digital gem.",
    "Penguins, the next NFT sensation.",
    "Claim your penguin, join the hype.",
    "Pixel penguins, endless vibes.",
    "Get your penguin, get ahead.",
    "Penguins taking over the blockchain!"
]

