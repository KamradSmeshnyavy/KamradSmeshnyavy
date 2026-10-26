<div align="center">

<img src="./assets/banner.svg" width="100%" alt="KAMRAD — ==Phrack Inc.== Volume 0x45, Issue 0x01"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=16&duration=2600&pause=900&color=00FF41&center=true&vCenter=true&width=640&height=30&lines=%24+.%2Fkamrad+--dissect+sample.exe;%5B*%5D+unpacking+UPX+layer...+done;%5B*%5D+anti-debug+tricks+identified%3A+4;%5B%2B%5D+C2+config+extracted+from+.rdata;%5B%2B%5D+YARA+rule+written.+next+sample+please." alt="typing"/>

<br/><br/>

<a href="https://t.me/Deny_kamrad_smeshnyavy"><img src="https://img.shields.io/badge/telegram-@Deny-0a0a0a?style=for-the-badge&logo=telegram&logoColor=00FF41&labelColor=0a0a0a"/></a>
<a href="https://t.me/WeekDaysSmeshnyavy"><img src="https://img.shields.io/badge/channel-WeekDays-0a0a0a?style=for-the-badge&logo=telegram&logoColor=FFB000&labelColor=0a0a0a"/></a>
<a href="https://open.spotify.com/user/cgd7kum73cyouiljqlogjikh7?si=c606775b542d4966"><img src="https://img.shields.io/badge/spotify-vibing-0a0a0a?style=for-the-badge&logo=spotify&logoColor=00FF41&labelColor=0a0a0a"/></a>
<img src="https://komarev.com/ghpvc/?username=KamradSmeshnyavy&style=for-the-badge&color=0a0a0a&label=VIEWS" alt="views"/>

</div>

```text
                              ==Phrack Inc.==

               Volume 0x45, Issue 0x01, Phile #0x01 of 0x07

|=-----------------------------------------------------------------------=|
|=--------------=[ K A M R A D    S M E S H N Y A V Y ]=-----------------=|
|=-----------------------------------------------------------------------=|

  0x01  Introduction ................................................ kamrad
  0x02  Arsenal: tools of the trade ................................. kamrad
  0x03  Recon: static analysis of ./kamrad .......................... kamrad
  0x04  Disassembly of self ......................................... kamrad
  0x05  Telemetry ................................................... kamrad
  0x06  Greetz & EOF ................................................ kamrad
```

<img src="./assets/section-0x01.svg" width="100%" alt="0x01 :: Introduction"/>

```text
--[ 1 - whoami

    Malware researcher, reverse engineer and low-level developer.

    I don't create malware. I dissect it.
    I don't break systems. I understand how they break.
    Low-level is not a skill level -- it's where the real code lives.

--[ 2 - current research

    [*] malware analysis   :: unpacking, anti-debug bypass, C2 config extraction
    [*] reverse engineering :: PE / ELF internals, packers, obfuscation
    [*] GNU/Linux          :: kernel internals, syscalls, tracing
    [*] tooling            :: Rust, C and x86-64 assembly

--[ 3 - fun fact

    `rm -rf /` doesn't work without `--no-preserve-root`.
```

> *"This is our world now... the world of the electron and the switch, the beauty of the baud."*
> — The Mentor, *The Conscience of a Hacker*, Phrack #7

<img src="./assets/section-0x02.svg" width="100%" alt="0x02 :: Arsenal"/>

<div align="center">

<img src="https://skillicons.dev/icons?i=c,cpp,rust,py,bash,lua,nix,js,html,css,linux,arch,neovim,vscode,git,sqlite,postgres,firebase&theme=dark&perline=9" alt="skills"/>

<br/><br/>

<img src="https://img.shields.io/badge/x86--64_asm-0a0a0a?style=for-the-badge&logo=intel&logoColor=00FF41"/>
<img src="https://img.shields.io/badge/ARM64-0a0a0a?style=for-the-badge&logo=arm&logoColor=00FF41"/>
<img src="https://img.shields.io/badge/AVR_asm-0a0a0a?style=for-the-badge&logo=arduino&logoColor=00FF41"/>
<img src="https://img.shields.io/badge/Nushell-0a0a0a?style=for-the-badge&logo=nushell&logoColor=00FF41"/>

<img src="https://img.shields.io/badge/IDA_Pro-0a0a0a?style=for-the-badge&logoColor=FFB000"/>
<img src="https://img.shields.io/badge/Ghidra-0a0a0a?style=for-the-badge&logoColor=FFB000"/>
<img src="https://img.shields.io/badge/radare2-0a0a0a?style=for-the-badge&logo=radar&logoColor=FFB000"/>
<img src="https://img.shields.io/badge/x64dbg-0a0a0a?style=for-the-badge&logoColor=FFB000"/>
<img src="https://img.shields.io/badge/GDB-0a0a0a?style=for-the-badge&logo=gnu&logoColor=FFB000"/>
<img src="https://img.shields.io/badge/angr-0a0a0a?style=for-the-badge&logo=python&logoColor=FFB000"/>

<img src="https://img.shields.io/badge/Wireshark-0a0a0a?style=for-the-badge&logo=wireshark&logoColor=00E5FF"/>
<img src="https://img.shields.io/badge/Nmap-0a0a0a?style=for-the-badge&logoColor=00E5FF"/>
<img src="https://img.shields.io/badge/Burp_Suite-0a0a0a?style=for-the-badge&logo=burpsuite&logoColor=00E5FF"/>
<img src="https://img.shields.io/badge/pwntools-0a0a0a?style=for-the-badge&logo=python&logoColor=00E5FF"/>
<img src="https://img.shields.io/badge/BlackArch-0a0a0a?style=for-the-badge&logo=archlinux&logoColor=00E5FF"/>

</div>

<details>
<summary><code>$ objdump -d ./skills.bin</code></summary>

```nasm
; ===============================================
; DISASSEMBLY OF skills.bin
; Architecture: x86-64 | ARM64 | AVR
; ===============================================

section .data
    arsenal:
        languages       db "C, C++, Rust, Python, x86-64 ASM, ARM64, AVR ASM"
        scripting       db "Bash, Nushell, Lua, Nix, JavaScript"
        markup          db "HTML, CSS, JSON, Markdown"

    tools:
        analysis        db "IDA Pro, Ghidra, radare2, x64dbg, gdb"
        monitoring      db "Wireshark, tcpdump, strace, ltrace, procmon"
        frameworks      db "pwntools, angr, Burp Suite"

    platforms:
        primary         db "GNU/Linux (Arch, Debian, NixOS)"
        secondary       db "Windows (for malware sandboxing)"
        editors         db "Neovim, VS Code"

    databases:
        storage         db "SQLite, PostgreSQL, Firebase"

section .text
    global _start
_start:
    mov rax, 0x1337
    lea rdi, [rel arsenal]
    call analyze_sample
    jmp _start              ; never stop learning
```

</details>

<img src="./assets/section-0x03.svg" width="100%" alt="0x03 :: Recon"/>

<div align="center">
<img src="./assets/recon.svg" width="90%" alt="static analysis of ./kamrad"/>
</div>

<img src="./assets/section-0x04.svg" width="100%" alt="0x04 :: Disassembly of self"/>

<div align="center">
<img src="./assets/disasm.svg" width="90%" alt="r2 disassembly of sym.main"/>
</div>

<img src="./assets/section-0x05.svg" width="100%" alt="0x05 :: Telemetry"/>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=KamradSmeshnyavy&show_icons=true&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=C8FFD4&icon_color=FFB000&ring_color=00FF41&custom_title=%24%20gh%20stats%20--user%20kamrad" height="170" alt="stats"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=KamradSmeshnyavy&layout=compact&langs_count=6&hide_border=true&bg_color=0a0a0a&title_color=00FF41&text_color=C8FFD4&custom_title=%24%20cloc%20.%2F*" height="170" alt="top languages"/>

<img src="https://streak-stats.demolab.com/?user=KamradSmeshnyavy&hide_border=true&background=0a0a0a&stroke=00FF41&ring=00FF41&fire=FFB000&currStreakNum=00FF41&sideNums=00FF41&currStreakLabel=C8FFD4&sideLabels=C8FFD4&dates=4F6355" width="70%" alt="streak"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KamradSmeshnyavy/KamradSmeshnyavy/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/KamradSmeshnyavy/KamradSmeshnyavy/output/github-snake.svg"/>
  <img alt="snake eating contributions" src="https://raw.githubusercontent.com/KamradSmeshnyavy/KamradSmeshnyavy/output/github-snake-dark.svg"/>
</picture>

</div>

<img src="./assets/section-0x06.svg" width="100%" alt="0x06 :: Greetz"/>

<div align="center">
<img src="./assets/footer.svg" width="100%" alt="EOF"/>
</div>
