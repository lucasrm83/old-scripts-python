import android
droid = android.Android()
title = "progress"
str = "loading"
droid.dialogCreateHorizontalProgress(title,str,100)
droid.showDialog()
    
for x in range(0,99):
    time.sleep(0.1)
    droid.dialogSetCurrentProgress(x)
    
droid.DialogDismiss()