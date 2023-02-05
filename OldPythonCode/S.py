import android
droid = android.Android() 
uname = droid.getInput("Enter your name")
droid.makeToast("Hello %s" %uname.result)