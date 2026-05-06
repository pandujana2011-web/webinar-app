
  from flask import Flask, render_template

  app = Flask(__name__)

  # CONFIGURATION - Change these!
  CLINIC_ADDRESS = "INSERT YOUR FULL CLINIC ADDRESS HERE"
  YOUTUBE_LINK = "https://www.youtube.com/@Nagavenkateswararao-s2o"
  RAZORPAY_LINK = "https://rzp.io/rzp/ZaUY9HgF"
  WEBINAR_LINK = "INSERT YOUR ZOOM/GOOGLE MEET LINK HERE"
  WHATSAPP_LINK = "INSERT YOUR WHATSAPP GROUP LINK HERE"

  @app.route('/')
  def home():
      # This is the public page (Clinic Address and YouTube)
      return render_template('index.html',
                             address=CLINIC_ADDRESS,
                             yt_link=YOUTUBE_LINK,
                             pay_link=RAZORPAY_LINK)

  @app.route('/payment-success')
  def success():
      # This page is only reached after payment
      return render_template('success.html',
                             webinar_link=WEBINAR_LINK,
                             whatsapp_link=WHATSAPP_LINK)

  if __name__ == '__main__':
      app.run(debug=True)
