class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        all_sprites = pygame.sprite.Group()
        pokemongroup = pygame.sprite.Group()
        bushesgroup = pygame.sprite.Group()
        wildpokemongroup = pygame.sprite.Group()

        Bush = BushesAndStuff()
        # all_sprites.add(Bush)
        bushesgroup.add(Bush)
        Bush2 = BushesAndStuff()
        # all_sprites.add(Bush2)
        bushesgroup.add(Bush2)
        Bush3 = BushesAndStuff()
        # all_sprites.add(Bush3)
        bushesgroup.add(Bush3)
        Bush4 = BushesAndStuff()
        # all_sprites.add(Bush4)
        bushesgroup.add(Bush4)
        Bush5 = BushesAndStuff()
        # all_sprites.add(Bush5)
        bushesgroup.add(Bush5)
        Bush6 = BushesAndStuff()
        # all_sprites.add(Bush6)
        bushesgroup.add(Bush6)
        Bush7 = BushesAndStuff()
        # all_sprites.add(Bush7)
        bushesgroup.add(Bush7)
        Bush8 = BushesAndStuff()
        # all_sprites.add(Bush8)
        bushesgroup.add(Bush8)
        Bush9 = BushesAndStuff()
        # all_sprites.add(Bush9)
        bushesgroup.add(Bush9)
        Bush10 = BushesAndStuff()
        # all_sprites.add(Bush10)
        bushesgroup.add(Bush10)
        Bush11 = BushesAndStuff()
        # all_sprites.add(Bush11)
        bushesgroup.add(Bush11)
        Bush12 = BushesAndStuff()
        # all_sprites.add(Bush12)
        bushesgroup.add(Bush12)
        Bush13 = BushesAndStuff()
        # all_sprites.add(Bush13)
        bushesgroup.add(Bush13)
        Bush14 = BushesAndStuff()
        # all_sprites.add(Bush14)
        bushesgroup.add(Bush14)
        Bush15 = BushesAndStuff()
        # all_sprites.add(Bush15)
        bushesgroup.add(Bush15)

        MyCharac = Guy()
        all_sprites.add(MyCharac)

        Pikachu = PichuEvo(5)
        pokemongroup.add(Pikachu)
        Wild_Pichu = RoamPichu(5)
        wildpokemongroup.add(Wild_Pichu)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(var.BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
