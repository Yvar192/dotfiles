{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  environment.pathsToLink = [ "/libexec" ]; # links /libexec from derivations to /run/current-system/sw

  # Use the systemd-boot EFI boot loader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  
  # Networking options.
  networking = {
	hostName = "nixos";
	networkmanager.enable = true;
  };

  # Enable automatic updates.
  system.autoUpgrade.channel = "https://nixos.org/channels/nixos-unstable/";
  system.autoUpgrade.enable = true;

  # Select internationalisation properties.
  i18n = {
  	consoleFont = "Lat2-Terminus16";
  	consoleKeyMap = "us";
  	defaultLocale = "en_US.UTF-8";
   };

  # Set your time zone.
  time.timeZone = "Europe/Amsterdam";

  # Allow unfree packages.
  nixpkgs.config.allowUnfree = true;

  # System packages.
  environment.systemPackages = with pkgs; [
    i3lock
    rxvt_unicode
    vim
    wget
    xorg.xmodmap
    xorg.xprop
    maim
    xclip
    dunst
    dmenu
    clipit
    networkmanagerapplet
    imagemagick
    nitrogen
    redshift
    playerctl
    perl
    speedtest-cli
    wine
    qutebrowser
    mpv
    discord
    spotify
    appimage-run
    transmission-gtk
    (steam.override { extraPkgs = pkgs: [ mono gtk3 gtk3-x11 libgdiplus zlib ]; nativeOnly = true; }).run
    snes9x-gtk
    libretro.mupen64plus
  ];

  # Always update the Linux packages to their latest versions.
  boot.kernelPackages = pkgs.linuxPackages_latest;

  # Enable the OpenSSH daemon.
  services.openssh.enable = true;
  
  # Configure hardware options.
  hardware = {
    opengl.enable = true;
    opengl.driSupport32Bit = true; # Required by some Steam games.
    pulseaudio.enable = true;
    pulseaudio.support32Bit = true; # Required by some Steam games.
  };

  # Configure the Xserver.
  services.xserver = {
	enable = true;
  	layout = "us";
  	xkbOptions = "eurosign:e";
	videoDrivers = [ "nvidiaBeta" ];
	displayManager.slim.enable = true;
	windowManager.i3.package = pkgs.i3-gaps;
	windowManager.i3.enable = true;
  };

  # Enable sound.
  sound.enable = true;

  # Define user accounts.
  users.users.ivar = {
  	isNormalUser = true;
  	extraGroups = [ "wheel" "networkmanager" ]; # Enable ‘sudo’ and network managing permissions for the user.
	shell = pkgs.zsh;
  };

  system.stateVersion = "20.03"; # Do not change unless told to. 
}
