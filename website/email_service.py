"""
Brevo Email Service for SZ Global Arabia Traders
Sends beautiful HTML email notifications when contact form is submitted
"""

import requests
from django.conf import settings
from datetime import datetime


def send_contact_notification(contact_data):
    """
    Send email notification when someone submits contact form
    
    Args:
        contact_data: dict with keys: name, email, phone, subject, message
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    
    # Check if API key is configured
    api_key = getattr(settings, 'BREVO_API_KEY', '')
    if not api_key:
        print("BREVO_API_KEY not configured. Email not sent.")
        return False
    
    # Brevo API endpoint
    url = "https://api.brevo.com/v3/smtp/email"
    
    # Headers
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }
    
    # Build beautiful HTML email
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f5f5;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #FFB86C 0%, #FF9F4A 100%); padding: 30px; border-radius: 15px 15px 0 0; text-align: center;">
                <h1 style="color: white; margin: 0; font-size: 28px; font-weight: 700;">
                    📧 New Contact Enquiry
                </h1>
                <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 14px;">
                    SZ Global Arabia Traders
                </p>
            </div>
            
            <!-- Main Content -->
            <div style="background: white; padding: 30px; border-radius: 0 0 15px 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <!-- Alert Badge -->
                <div style="background: #FFF3E0; border-left: 4px solid #FFB86C; padding: 15px; border-radius: 5px; margin-bottom: 25px;">
                    <p style="margin: 0; color: #E65100; font-weight: 600;">
                        🔔 You have received a new enquiry from your website!
                    </p>
                </div>
                
                <!-- Customer Details -->
                <h2 style="color: #333; font-size: 18px; margin-bottom: 20px; border-bottom: 2px solid #FFB86C; padding-bottom: 10px;">
                    👤 Customer Details
                </h2>
                
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee; width: 35%;">
                            <strong style="color: #666;">Name:</strong>
                        </td>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee; color: #333;">
                            {contact_data.get('name', 'N/A')}
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee;">
                            <strong style="color: #666;">Email:</strong>
                        </td>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee;">
                            <a href="mailto:{contact_data.get('email', '')}" style="color: #FFB86C; text-decoration: none;">
                                {contact_data.get('email', 'N/A')}
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee;">
                            <strong style="color: #666;">Phone:</strong>
                        </td>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee; color: #333;">
                            {contact_data.get('phone', 'Not provided')}
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee;">
                            <strong style="color: #666;">Subject:</strong>
                        </td>
                        <td style="padding: 12px 0; border-bottom: 1px solid #eee; color: #333; font-weight: 600;">
                            {contact_data.get('subject', 'N/A')}
                        </td>
                    </tr>
                </table>
                
                <!-- Message Section -->
                <h2 style="color: #333; font-size: 18px; margin: 25px 0 15px 0; border-bottom: 2px solid #FFB86C; padding-bottom: 10px;">
                    💬 Message
                </h2>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #FFB86C;">
                    <p style="margin: 0; color: #333; line-height: 1.8; white-space: pre-wrap;">
                        {contact_data.get('message', 'No message provided')}
                    </p>
                </div>
                
                <!-- Timestamp -->
                <div style="margin-top: 25px; padding-top: 20px; border-top: 1px solid #eee; text-align: center;">
                    <p style="color: #999; font-size: 12px; margin: 0;">
                        📅 Received on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
                    </p>
                </div>
                
                <!-- Action Button -->
                <div style="text-align: center; margin-top: 25px;">
                    <a href="mailto:{contact_data.get('email', '')}" 
                       style="display: inline-block; background: linear-gradient(135deg, #FFB86C 0%, #FF9F4A 100%); color: white; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: 600; box-shadow: 0 4px 15px rgba(255,184,108,0.4);">
                        Reply to {contact_data.get('name', 'Customer').split()[0]}
                    </a>
                </div>
            </div>
            
            <!-- Footer -->
            <div style="text-align: center; padding: 20px; color: #999; font-size: 12px;">
                <p style="margin: 0;">
                    This is an automated notification from SZ Global Arabia Traders website.
                </p>
                <p style="margin: 5px 0 0 0;">
                    © {datetime.now().year} SZ Global Arabia Traders | Greater Noida, India
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Plain text version
    text_content = f"""
    New Contact Enquiry - SZ Global Arabia Traders
    
    Customer Details:
    - Name: {contact_data.get('name', 'N/A')}
    - Email: {contact_data.get('email', 'N/A')}
    - Phone: {contact_data.get('phone', 'Not provided')}
    - Subject: {contact_data.get('subject', 'N/A')}
    
    Message:
    {contact_data.get('message', 'No message provided')}
    
    Received on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
    """
    
    # Email payload
    payload = {
        "sender": {
            "name": getattr(settings, 'SENDER_NAME', 'SZ Global Arabia Traders'),
            "email": getattr(settings, 'SENDER_EMAIL', 'info@szglobalarabia.com')
        },
        "to": [
            {
                "email": getattr(settings, 'NOTIFICATION_EMAIL', 'info@szglobalarabia.com'),
                "name": "SZ Global Team"
            }
        ],
        "subject": f"🔔 New Enquiry: {contact_data.get('subject', 'Contact Form Submission')}",
        "htmlContent": html_content,
        "textContent": text_content
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            print(f"Email sent successfully! Message ID: {response.json().get('messageId')}")
            return True
        else:
            print(f"Failed to send email. Status: {response.status_code}, Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
