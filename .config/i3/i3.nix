pkgs:
let
  mod = "Mod4";
  keys = import ./keybindings.nix mod; #TODO: Define workspaces somewhere, not sure how to pass multiple vars to an import?

  # Colors
  backgroundColor = "#2f343f";
  textColor = "#ffffff";
  inactiveTextColor = "#676e7d";
in
{
  package = pkgs.i3-gaps;
  enable = true;

  config = {
    modifier = mod;
    keybindings = keys;
    fonts = [ "Liberation Sans 10" ];

    gaps = {
      inner = 4;
      outer = 4;
    };

    # Disable default resize mode
    modes = {};

    terminal = "st";

    window.commands = [
      { command = "border pixel 1"; criteria = { class = "^.*"; }; }
      { command = "move to workspace 4: Spotify"; criteria = { class = "Spotify"; }; }
    ];

    startup = [
      { command = "--no-startup-id amixer set Master 35%"; always = false; }
      { command = "--no-startup-id xmodmap -e 'remove Lock = Caps_Lock' -e 'keysym Caps_Lock = Escape'"; always = true; }
      { command = "--no-startup-id redshift -l 50.77083:3.57361"; always = false; }
      { command = "--no-startup-id xrandr --output DVI-D-0 --off --output HDMI-0 --mode 1280x1024 --pos 4720x570 --rotate normal --output DP-0 --mode 3440x1440 --pos 1280x0 --rotate normal --output DP-1 --off --primary"; always = true; }
      { command = "--no-startup-id nitrogen --restore"; always = true; }
    ];

    assigns = {
      "2: Media" = [ { class = "electronplayer"; } ];
      "3: Discord" = [ { class = "discord"; } ];
      "5: Games" = [ { class = "Steam"; } ];
      "10: Torrent" = [ { class = "Transmission-gtk"; } ];
    };

    colors = {
      focused = { background = "#81848c"; border = "#81848c"; childBorder = "#81848c"; text = textColor; indicator = "#81848c"; };
      focusedInactive = { background = backgroundColor; border = backgroundColor; childBorder = backgroundColor; text = inactiveTextColor; indicator = backgroundColor; };
      unfocused = { background = backgroundColor; border = backgroundColor; childBorder = backgroundColor; text = inactiveTextColor; indicator = backgroundColor; };
      urgent = { background = "#e53935"; border = "e53935"; childBorder = "e53935"; text = textColor; indicator = backgroundColor; };
    };

    bars = [ { 
      statusCommand = "${pkgs.i3blocks}/bin/i3blocks -c ~/.config/i3/i3blocks.conf";
      fonts = [ "Liberation Sans 10" ];
      position = "top";
      colors = {
        background = backgroundColor;
        separator = "757575";
        focusedWorkspace = { background = backgroundColor; border = backgroundColor; text = textColor; };
        activeWorkspace = { background = backgroundColor; border = backgroundColor; text = textColor; };
        inactiveWorkspace = { background = backgroundColor; border = backgroundColor; text = inactiveTextColor; };
        urgentWorkspace = { background = "#e53935"; border = "e53935"; text = textColor; };
      };
    } ];
  };
}