#creates a manifest named “killmenow” that kills a process
exec { “killmenow”:
    command => “pkill killmenow”,
    path    => “/usr/bin”,
}
