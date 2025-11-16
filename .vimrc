syntax on
filetype plugin indent on

" Basic setup
set number
set autoindent
set mouse=a
"set clipboard=unnamedplus

" Python specific (4 spaces)
set tabstop=4
set shiftwidth=4
set expandtab

" Smart search
set ignorecase
set smartcase

" Auto-pairing brackets
inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>
inoremap " ""<Left>
inoremap ' ''<Left>

" Auto-load CP template for new .py files
augroup CPTemplate
    autocmd!
    autocmd BufNewFile *.py 0r ~/template.py | /<<<START>>>/ | normal! cc
augroup END

if has('unix')
    " For Linux / macOS
    nnoremap <F5> :w !python % < /dev/tty<CR>
else
    " For Windows (CON is the equivalent of /dev/tty)
    nnoremap <F5> :w !python % < CON<CR>
endif
