; NSIS Installer Script for Koromali
; Generated dynamically by the Installer Builder plugin.

;================================
;==         DEFINES            ==
; APP_NAME, APP_VERSION, APP_AUTHOR, MAIN_EXE, OUT_FILE, ASSETS_DIR,
; INSTALLER_ICON, LICENSE_FILE, BUILD_SOURCE_DIR are passed via makensis /D
;================================
!ifndef APP_NAME
  !error "APP_NAME must be defined (pass /DAPP_NAME=... to makensis)"
!endif
!ifndef MAIN_EXE
  !define MAIN_EXE "Koromali.exe"
!endif
!define PRODUCT_NAME "${APP_NAME}"
!define PRODUCT_VERSION "${APP_VERSION}"
!define PRODUCT_AUTHOR "${APP_AUTHOR}"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"

;================================
;==       MUI SETTINGS         ==
;================================
!include "MUI2.nsh"
!define MUI_ABORTWARNING
!define MUI_ICON "${INSTALLER_ICON}"
!define MUI_UNICON "${INSTALLER_ICON}"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "${ASSETS_DIR}/header.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP "${ASSETS_DIR}/welcome.bmp"
!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_EXE}"

;================================
;==        PAGE SETUP          ==
;================================
!insertmacro MUI_PAGE_WELCOME
!ifdef LICENSE_FILE
    !insertmacro MUI_PAGE_LICENSE "${LICENSE_FILE}"
!endif
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "${OUT_FILE}"
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"
ShowInstDetails show
SetCompressor lzma
SetShellVarContext all

; --- DYNAMIC CONTENT INJECTED BY BUILD SCRIPT ---
!GENERATED_CONTENT_GOES_HERE!


; --- DYNAMIC FUNCTIONS INJECTED BY BUILD SCRIPT ---
!GENERATED_FUNCTIONS_GOES_HERE!


Function FinishPagePrompt
  MessageBox MB_YESNO|MB_ICONQUESTION "Do you want to set Koromali as the default application for common code file types (.py, .js, .txt, etc.)?" /SD IDYES IDYES Register IDNO DontRegister
  Register:
    Call RegisterFileAssociations
  DontRegister:
FunctionEnd

Function .onInit
  ; Registry entries for Add/Remove Programs
  WriteRegStr HKLM "${PRODUCT_UNINST_KEY}" "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr HKLM "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_AUTHOR}"
  WriteRegStr HKLM "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\${MAIN_EXE}"
  WriteRegDWORD HKLM "${PRODUCT_UNINST_KEY}" "NoModify" 1
  WriteRegDWORD HKLM "${PRODUCT_UNINST_KEY}" "NoRepair" 1
  WriteRegStr HKLM "${PRODUCT_UNINST_KEY}" "UninstallString" '"$INSTDIR\uninstall.exe"'
FunctionEnd

Function un.onInit
    SetShellVarContext all
FunctionEnd