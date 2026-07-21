; NSIS Installer Script for Koromali
; Generated dynamically by the Installer Builder / CI build script.
;
; APP_NAME, APP_VERSION, APP_AUTHOR, MAIN_EXE, OUT_FILE, ASSETS_DIR,
; INSTALLER_ICON, LICENSE_FILE, BUILD_SOURCE_DIR are passed via makensis /D

Unicode true
SetCompressor /SOLID lzma

!ifndef APP_NAME
  !error "APP_NAME must be defined (pass /DAPP_NAME=... to makensis)"
!endif
!ifndef MAIN_EXE
  !define MAIN_EXE "Koromali.exe"
!endif
!ifndef APP_VERSION
  !define APP_VERSION "0.0.0"
!endif
!ifndef APP_AUTHOR
  !define APP_AUTHOR "Koromali"
!endif

!define PRODUCT_NAME "${APP_NAME}"
!define PRODUCT_VERSION "${APP_VERSION}"
!define PRODUCT_AUTHOR "${APP_AUTHOR}"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "${OUT_FILE}"
InstallDir "$PROGRAMFILES64\${PRODUCT_NAME}"
ShowInstDetails show
RequestExecutionLevel admin

!include "MUI2.nsh"
!define MUI_ABORTWARNING
!define MUI_ICON "${INSTALLER_ICON}"
!define MUI_UNICON "${INSTALLER_ICON}"
!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_EXE}"

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

; --- DYNAMIC CONTENT INJECTED BY BUILD SCRIPT ---
!GENERATED_CONTENT_GOES_HERE!


; --- DYNAMIC FUNCTIONS INJECTED BY BUILD SCRIPT ---
!GENERATED_FUNCTIONS_GOES_HERE!


Function .onInit
  SetShellVarContext all
FunctionEnd

Function .onInstSuccess
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
