// SZ Global Arabia Traders - Intelligent Chat Assistant
// Knowledge base about products and company

const chatKnowledge = {
    // Company Information
    company: {
        name: "SZ Global Arabia Traders",
        location: "Greater Noida, Uttar Pradesh, India",
        email: "info@szglobalarabia.com",
        experience: "5+ years",
        description: "Premier import-export company specializing in premium agricultural products, timber, industrial equipment, and safety gear.",
        services: ["Export", "Import", "Bulk Orders", "Custom Packaging", "Quality Assurance"]
    },

    // Rice Products
    rice: {
        intro: "We export premium Basmati rice from India, known for its long grains, aromatic fragrance, and superior quality.",
        types: [
            {
                name: "1121 Golden Premium Sella Rice",
                description: "The crown jewel of Basmati rice with extra-long grains (8.3mm+). Golden color from parboiling process.",
                features: ["Extra Long Grain", "Golden Color", "Non-Sticky", "Aromatic"],
                origin: "Punjab & Haryana, India",
                uses: "Biryani, Pulao, Premium Dishes"
            },
            {
                name: "1509 Creamy Basmati Rice",
                description: "Beautiful creamy white color with long grains (7.5mm+). Popular for everyday cooking.",
                features: ["Long Grain", "Creamy White", "Fluffy Texture", "Aromatic"],
                origin: "North India",
                uses: "Daily Rice, Jeera Rice, Fried Rice"
            },
            {
                name: "All Type Basmati Rice",
                description: "Complete range including Traditional, Pusa, Sugandha, and PR varieties for different market segments.",
                features: ["Multiple Varieties", "Cost Effective", "Bulk Available"],
                origin: "Various regions, India"
            }
        ],
        certifications: ["ISO 22000", "FSSAI", "APEDA Certified"],
        packaging: ["1kg", "5kg", "10kg", "25kg", "50kg bags"],
        moq: "Minimum order: 1 container (25-27 MT)"
    },

    // Spices Products
    spices: {
        intro: "Premium Indian spices sourced directly from farms in Kerala, Karnataka, and Rajasthan. 100% natural, no additives.",
        types: [
            {
                name: "Cinnamon (Dalchini)",
                description: "Premium quality cinnamon sticks from Kerala and Karnataka. Sweet, warm aroma.",
                features: ["High Oil Content", "Hand Selected", "Rich Aroma"],
                origin: "Kerala & Karnataka, India",
                uses: "Curries, Biryani, Garam Masala, Tea, Baking"
            },
            {
                name: "Coriander Seeds (Dhaniya)",
                description: "Bright, citrusy flavor coriander from Rajasthan and Gujarat - world's largest producers.",
                features: ["Machine Cleaned", "Sun Dried", "Uniform Size"],
                origin: "Rajasthan & Gujarat, India",
                uses: "Curry Powders, Pickles, Chutneys"
            },
            {
                name: "Clove (Laung)",
                description: "Aromatic flower buds from Kerala spice gardens. Strong, warm, pungent aroma.",
                features: ["High Eugenol Content", "Hand Picked", "Medicinal Grade"],
                origin: "Kerala, India",
                uses: "Biryani, Garam Masala, Chai Tea, Dental Care"
            }
        ],
        certifications: ["ISO 22000", "HACCP", "FSSAI", "Spices Board Approved"],
        quality: "Purity 99% minimum, Moisture 12% maximum"
    },

    // Plywood Products
    plywood: {
        intro: "High-quality plywood sheets manufactured from sustainable Indian timber. Perfect for construction and furniture.",
        types: [
            {
                name: "4x4 Feet Plywood",
                description: "Standard size sheets for large construction projects. Size: 1220 x 1220mm.",
                thickness: "6mm to 25mm",
                grades: ["BWR", "BWP", "MR"]
            },
            {
                name: "2x2 Feet Plywood",
                description: "Compact sheets for small projects and DIY work. Size: 610 x 610mm.",
                thickness: "4mm to 18mm",
                grades: ["Commercial", "Marine"]
            }
        ],
        plywoodTypes: ["Commercial Plywood", "Marine Plywood (Waterproof)", "BWR Plywood"],
        certifications: ["IS 303", "IS 710", "Zero Formaldehyde"],
        cores: ["Hardwood", "Eucalyptus", "Gurjan Face"]
    },

    // Industrial Products
    industrial: {
        intro: "Quality industrial equipment and machinery for manufacturing, construction, and various industrial applications.",
        categories: [
            {
                name: "Manufacturing Machinery",
                items: ["CNC Machines", "Packaging Equipment", "Conveyor Systems", "Welding Machines"]
            },
            {
                name: "Construction Equipment",
                items: ["Excavators", "Concrete Mixers", "Scaffolding", "Tower Cranes"]
            },
            {
                name: "Power Tools",
                items: ["Drills", "Angle Grinders", "Cutting Machines", "Sanders"]
            },
            {
                name: "Material Handling",
                items: ["Forklifts", "Pallet Jacks", "Cranes", "Hoists"]
            }
        ],
        services: ["Technical Support", "Installation", "Training", "Spare Parts"]
    },

    // Safety Shoes
    safetyShoes: {
        intro: "Premium leather safety shoes designed for worker protection. Steel toe caps, slip-resistant soles.",
        types: [
            {
                name: "Steel Toe Safety Boots",
                description: "Maximum protection with 200J impact rated steel toe caps. Genuine leather.",
                features: ["Steel Toe (200J)", "Oil Resistant", "Anti-Slip", "Ankle Support"]
            },
            {
                name: "Low-Cut Safety Shoes",
                description: "Comfortable everyday wear with essential toe protection.",
                features: ["Lightweight", "Breathable", "Modern Design"]
            },
            {
                name: "Composite Toe Shoes",
                description: "Non-metal protection for electrical environments. 40% lighter than steel.",
                features: ["Non-Metallic", "EH Rated", "Airport Friendly"]
            },
            {
                name: "Waterproof Safety Boots",
                description: "Weather-resistant for outdoor and wet conditions.",
                features: ["Waterproof Membrane", "Insulated Options", "Extended Height"]
            }
        ],
        certifications: ["EN ISO 20345", "ASTM F2413", "IS 15298", "CE Certified"],
        industries: ["Construction", "Manufacturing", "Mining", "Warehousing"],
        customization: ["Logo Branding", "Custom Colors", "Private Labeling"]
    },

    // FAQs
    faqs: {
        shipping: "We ship worldwide. Typical delivery time is 15-30 days depending on destination. We handle all export documentation.",
        moq: "Minimum order varies by product. For rice: 1 container (25-27 MT). For spices: 500kg. For plywood: 1 container. For smaller orders, please contact us.",
        payment: "We accept LC (Letter of Credit), TT (Bank Transfer), and other standard international payment methods.",
        samples: "Yes, we provide samples for quality assessment. Sample cost may apply depending on the product.",
        quality: "All products undergo rigorous quality checks. We are ISO certified and comply with international standards.",
        quote: "You can request a quote through our Contact page or email us at info@szglobalarabia.com"
    }
};

// Chat responses generator
function generateResponse(userMessage) {
    const msg = userMessage.toLowerCase().trim();
    
    // Greetings
    if (msg.match(/^(hi|hello|hey|namaste|good morning|good afternoon|good evening)/)) {
        return `Hello! 👋 Welcome to SZ Global Arabia Traders. I'm your virtual assistant. How can I help you today?\n\nI can help you with:\n• Rice products (Basmati varieties)\n• Spices (Cinnamon, Coriander, Clove)\n• Plywood sheets\n• Industrial equipment\n• Safety shoes\n• Pricing & quotes\n• Shipping information`;
    }

    // Company info
    if (msg.match(/company|about|who are you|tell me about/)) {
        return `🏢 **SZ Global Arabia Traders**\n\n${chatKnowledge.company.description}\n\n📍 Location: ${chatKnowledge.company.location}\n📧 Email: ${chatKnowledge.company.email}\n⏱️ Experience: ${chatKnowledge.company.experience}\n\nWe specialize in exporting premium Indian products worldwide!`;
    }

    // Rice queries
    if (msg.match(/rice|basmati|1121|1509|chawal/)) {
        if (msg.match(/1121|golden|sella/)) {
            const rice = chatKnowledge.rice.types[0];
            return `🍚 **${rice.name}**\n\n${rice.description}\n\n✅ Features: ${rice.features.join(", ")}\n🌾 Origin: ${rice.origin}\n🍽️ Best For: ${rice.uses}\n\nWould you like pricing or sample information?`;
        }
        if (msg.match(/1509|creamy/)) {
            const rice = chatKnowledge.rice.types[1];
            return `🍚 **${rice.name}**\n\n${rice.description}\n\n✅ Features: ${rice.features.join(", ")}\n🌾 Origin: ${rice.origin}\n🍽️ Best For: ${rice.uses}`;
        }
        return `🍚 **Premium Basmati Rice**\n\n${chatKnowledge.rice.intro}\n\n**Our Rice Varieties:**\n1. 1121 Golden Premium Sella Rice (8.3mm+ grains)\n2. 1509 Creamy Basmati Rice (7.5mm+ grains)\n3. All Type Basmati Rice (Various)\n\n📦 Packaging: ${chatKnowledge.rice.packaging.join(", ")}\n📋 MOQ: ${chatKnowledge.rice.moq}\n\nWhich variety would you like to know more about?`;
    }

    // Spices queries
    if (msg.match(/spice|masala|cinnamon|dalchini|coriander|dhaniya|clove|laung/)) {
        if (msg.match(/cinnamon|dalchini/)) {
            const spice = chatKnowledge.spices.types[0];
            return `🌿 **${spice.name}**\n\n${spice.description}\n\n✅ Features: ${spice.features.join(", ")}\n🌾 Origin: ${spice.origin}\n🍽️ Uses: ${spice.uses}`;
        }
        if (msg.match(/coriander|dhaniya/)) {
            const spice = chatKnowledge.spices.types[1];
            return `🌿 **${spice.name}**\n\n${spice.description}\n\n✅ Features: ${spice.features.join(", ")}\n🌾 Origin: ${spice.origin}\n🍽️ Uses: ${spice.uses}`;
        }
        if (msg.match(/clove|laung/)) {
            const spice = chatKnowledge.spices.types[2];
            return `🌿 **${spice.name}**\n\n${spice.description}\n\n✅ Features: ${spice.features.join(", ")}\n🌾 Origin: ${spice.origin}\n🍽️ Uses: ${spice.uses}`;
        }
        return `🌿 **Premium Indian Spices**\n\n${chatKnowledge.spices.intro}\n\n**Our Spices:**\n1. 🟤 Cinnamon (Dalchini) - Kerala & Karnataka\n2. 🟡 Coriander Seeds (Dhaniya) - Rajasthan\n3. 🟤 Clove (Laung) - Kerala\n\n📋 Quality: ${chatKnowledge.spices.quality}\n🏆 Certifications: ${chatKnowledge.spices.certifications.join(", ")}\n\nWhich spice interests you?`;
    }

    // Plywood queries
    if (msg.match(/plywood|wood|timber|4x4|2x2/)) {
        return `🪵 **Premium Plywood Sheets**\n\n${chatKnowledge.plywood.intro}\n\n**Available Sizes:**\n📐 4x4 Feet (1220x1220mm) - Thickness: 6mm-25mm\n📐 2x2 Feet (610x610mm) - Thickness: 4mm-18mm\n\n**Types:**\n• Commercial Plywood (MR Grade)\n• Marine Plywood (Waterproof)\n• BWR Plywood (Boiling Water Resistant)\n\n🏆 Certifications: IS 303, IS 710 Certified\n🌳 Cores: Hardwood, Eucalyptus, Gurjan`;
    }

    // Industrial queries
    if (msg.match(/industrial|machinery|machine|equipment|power tool|forklift|crane|cnc/)) {
        return `🏭 **Industrial Equipment**\n\n${chatKnowledge.industrial.intro}\n\n**Categories:**\n⚙️ Manufacturing Machinery\n🏗️ Construction Equipment\n🔧 Power Tools\n📦 Material Handling\n\n✅ Services: ${chatKnowledge.industrial.services.join(", ")}\n\nWhat type of equipment are you looking for?`;
    }

    // Safety shoes queries
    if (msg.match(/safety|shoe|boot|footwear|steel toe|composite/)) {
        return `👟 **Safety Shoes**\n\n${chatKnowledge.safetyShoes.intro}\n\n**Our Range:**\n1. Steel Toe Safety Boots (200J protection)\n2. Low-Cut Safety Shoes (Lightweight)\n3. Composite Toe Shoes (Non-metallic)\n4. Waterproof Safety Boots\n\n🏆 Certifications: EN ISO 20345, ASTM F2413\n🏭 Industries: Construction, Manufacturing, Mining\n\n✨ Custom branding and private labeling available!`;
    }

    // Pricing/Quote
    if (msg.match(/price|pricing|cost|rate|quote|quotation/)) {
        return `💰 **Pricing Information**\n\nPrices vary based on:\n• Product type and quantity\n• Packaging requirements\n• Destination country\n• Shipping method\n\n📝 For a detailed quote, please:\n1. Visit our Contact page\n2. Email: info@szglobalarabia.com\n3. Specify products, quantity, and destination\n\nWe typically respond within 24 hours! Would you like me to guide you to the contact page?`;
    }

    // Shipping/Delivery
    if (msg.match(/ship|shipping|delivery|export|import|time|days/)) {
        return `🚢 **Shipping Information**\n\n${chatKnowledge.faqs.shipping}\n\n📦 We handle:\n• Export documentation\n• Customs clearance\n• Container loading\n• Insurance (optional)\n\n🌍 We export to 50+ countries worldwide!\n\nNeed shipping to a specific country?`;
    }

    // MOQ/Minimum Order
    if (msg.match(/moq|minimum|order quantity/)) {
        return `📦 **Minimum Order Quantities**\n\n${chatKnowledge.faqs.moq}\n\n• Rice: 25-27 MT (1 container)\n• Spices: 500kg minimum\n• Plywood: 1 container\n• Safety Shoes: 100 pairs\n\nFor smaller trial orders, please contact us!`;
    }

    // Sample request
    if (msg.match(/sample|try|test/)) {
        return `📦 **Sample Request**\n\n${chatKnowledge.faqs.samples}\n\nTo request samples:\n1. Email: info@szglobalarabia.com\n2. Specify product(s) needed\n3. Provide shipping address\n\nWe'll arrange samples after initial discussion!`;
    }

    // Payment
    if (msg.match(/payment|pay|lc|letter of credit|bank/)) {
        return `💳 **Payment Methods**\n\n${chatKnowledge.faqs.payment}\n\n• LC (Letter of Credit) ✓\n• TT (Bank Transfer) ✓\n• Advance Payment ✓\n\nPayment terms can be discussed based on order value and relationship.`;
    }

    // Certificate/Quality
    if (msg.match(/certificate|certification|quality|iso|standard/)) {
        return `🏆 **Quality & Certifications**\n\n${chatKnowledge.faqs.quality}\n\n**Our Certifications:**\n✅ ISO 9001:2015\n✅ ISO 22000 (Food Safety)\n✅ HACCP Certified\n✅ FSSAI Licensed\n✅ APEDA Registered\n\nAll products meet international quality standards!`;
    }

    // Contact
    if (msg.match(/contact|email|phone|call|reach|talk/)) {
        return `📞 **Contact Us**\n\n📍 Location: Greater Noida, Uttar Pradesh, India\n📧 Email: info@szglobalarabia.com\n🌐 Website: www.szglobalarabia.com\n\n⏰ Business Hours:\nMon-Fri: 9:00 AM - 6:00 PM\nSat: 9:00 AM - 2:00 PM\n\nOr visit our Contact page to send a message!`;
    }

    // Products overview
    if (msg.match(/product|what do you sell|what you have|catalog/)) {
        return `📦 **Our Products**\n\n🍚 **Rice** - Premium Basmati varieties\n🌿 **Spices** - Cinnamon, Coriander, Clove\n🪵 **Plywood** - 4x4, 2x2 sheets\n🏭 **Industrial** - Machinery & Equipment\n👟 **Safety Shoes** - All types\n\nAll products sourced from India with quality certification!\n\nWhich category interests you?`;
    }

    // Thanks
    if (msg.match(/thank|thanks|thx|appreciate/)) {
        return `You're welcome! 😊\n\nIs there anything else I can help you with? Feel free to ask about:\n• Products\n• Pricing\n• Shipping\n• Samples\n\nOr visit our Contact page for detailed inquiries!`;
    }

    // Bye
    if (msg.match(/bye|goodbye|see you|exit|close/)) {
        return `Thank you for chatting with us! 👋\n\nIf you need any assistance in the future, I'm here 24/7!\n\n📧 Email: info@szglobalarabia.com\n🌐 Visit our website anytime!\n\nHave a great day! 🌟`;
    }

    // Default response
    return `I'm not sure I understood that completely. 🤔\n\nI can help you with:\n• 🍚 Rice products\n• 🌿 Spices (Cinnamon, Coriander, Clove)\n• 🪵 Plywood sheets\n• 🏭 Industrial equipment\n• 👟 Safety shoes\n• 💰 Pricing & quotes\n• 🚢 Shipping info\n• 📞 Contact details\n\nPlease try asking about any of these topics, or contact us at info@szglobalarabia.com for specific queries!`;
}

// Initialize chat when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const chatWidget = document.getElementById('chat-widget');
    const chatToggle = document.getElementById('chat-toggle');
    const chatClose = document.getElementById('chat-close');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');

    // Toggle chat widget
    if (chatToggle) {
        chatToggle.addEventListener('click', () => {
            chatWidget.classList.toggle('hidden');
            chatToggle.classList.toggle('hidden');
            if (!chatWidget.classList.contains('hidden')) {
                chatInput.focus();
            }
        });
    }

    // Close chat
    if (chatClose) {
        chatClose.addEventListener('click', () => {
            chatWidget.classList.add('hidden');
            chatToggle.classList.remove('hidden');
        });
    }

    // Send message function
    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Show typing indicator
        showTyping();

        // Generate and show response after delay
        setTimeout(() => {
            hideTyping();
            const response = generateResponse(message);
            addMessage(response, 'bot');
        }, 800 + Math.random() * 500);
    }

    // Add message to chat
    function addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `flex ${type === 'user' ? 'justify-end' : 'justify-start'} mb-4`;
        
        const bubble = document.createElement('div');
        bubble.className = type === 'user' 
            ? 'bg-gradient-to-r from-light-orange to-dark-orange text-white px-4 py-3 rounded-2xl rounded-br-sm max-w-[80%] shadow-md'
            : 'bg-gray-100 text-gray-800 px-4 py-3 rounded-2xl rounded-bl-sm max-w-[80%] shadow-md';
        
        // Format message with markdown-like syntax
        bubble.innerHTML = content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
        
        messageDiv.appendChild(bubble);
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Typing indicator
    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'flex justify-start mb-4';
        typingDiv.innerHTML = `
            <div class="bg-gray-100 px-4 py-3 rounded-2xl rounded-bl-sm shadow-md">
                <div class="flex gap-1">
                    <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                    <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.1s"></div>
                    <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
                </div>
            </div>
        `;
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function hideTyping() {
        const typing = document.getElementById('typing-indicator');
        if (typing) typing.remove();
    }

    // Event listeners
    if (chatSend) {
        chatSend.addEventListener('click', sendMessage);
    }

    if (chatInput) {
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    }

    // Add welcome message on first open
    let welcomed = false;
    if (chatToggle) {
        chatToggle.addEventListener('click', () => {
            if (!welcomed && !chatWidget.classList.contains('hidden')) {
                setTimeout(() => {
                    addMessage("Hello! 👋 Welcome to SZ Global Arabia Traders!\n\nI'm your virtual assistant. How can I help you today?\n\nYou can ask me about:\n• Rice varieties\n• Spices\n• Plywood\n• Industrial equipment\n• Safety shoes\n• Pricing & shipping", 'bot');
                }, 500);
                welcomed = true;
            }
        });
    }
});
