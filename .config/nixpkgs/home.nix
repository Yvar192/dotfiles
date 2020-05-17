{ config, pkgs, ... }:
let
  requiredPackages = import ./requiredPackages.nix;
  stBuild = pkgs.callPackage ../st { };
  vimSettings = import ../nvim/nvim.nix;
  quteSettings = import ../qutebrowser/qutebrowser.nix;
  dunstSettings = import ../dunst/dunst.nix;
  i3Settings = import ../i3/i3.nix;
in
{
  nixpkgs = {
    config.allowUnfree = true;
    config.packageOverrides = pkgs: {
      dmenu = pkgs.dmenu.override {
        patches = [
          ../dmenu/dmenu-xresources-20200302.patch
        ];
      };
      st = stBuild;
    };
  };

  home.packages = with pkgs; requiredPackages pkgs ++ [
    # General utils
    unar unzip
    cmake gnumake
    wget
    git
    htop
    neofetch
    tree

    # Nix specific utils
    nix-index
    nix-prefetch-git

    # Games
    snes9x-gtk mupen64plus dolphinEmu
    steam

    # Media
    kdenlive obs-studio
    ncspot spotify
    firefox # Have to keep this installed for the 1password extension, unfortunately
    tor-browser-bundle-bin
    mpv
    ffmpeg

    # Applications
    pavucontrol
    lxappearance
    arc-theme
    capitaine-cursors
    arc-icon-theme
    discord
    transmission-gtk
    pentablet-driver
    mupdf
  ];

 programs = {
    home-manager.enable = true;
    neovim = vimSettings pkgs;
    qutebrowser = quteSettings;
  };

  xresources.properties = {
    "foreground" = "#F8F8F2";
    "background" = "#282A36";
    "color0" = "#000000";
    "color1" = "#FF5555";
    "color2" = "#50FA7B";
    "color3" = "#F1FA8C";
    "color4" = "#BD93F9";
    "color5" = "#FF79C6";
    "color6" = "#8BE9FD";
    "color7" = "#BFBFBF";
    "color8" = "#4D4D4D";
    "color9" = "#FF6E67";
    "color10" = "#5AF78E";
    "color11" = "#F4F99D";
    "color12" = "#CAA9FA";
    "color13" = "#FF92D0";
    "color14" = "#9AEDFE";
    "color15" = "#E6E6E6";
  };

  services.dunst = dunstSettings;

  xsession = {
    enable = true;
    scriptPath = ".hm-xsession";
    windowManager.i3 = i3Settings pkgs;
  };

  home.stateVersion = "20.09";
}
