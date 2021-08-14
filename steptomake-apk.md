===Membuat file .jks
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias

===bundle apk menjadi aligned.apk
zipalign -v -p 4 my-app-unsigned.apk my-app-unsigned-aligned.apk

===didaftarkan menjadi versi release.apk
apksigner sign --ks my-release-key.jks --out my-app-release.apk my-app-unsigned-aligned.apk

===verifikasi apk
apksigner verify my-app-release.apk