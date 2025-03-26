import pygame
import chess
import chess.engine
pygame.init()

# Ustawienia planszy
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (125, 135, 150)
CIRCLE_COLOR = (200, 0, 0)
FONT_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Szachy drobna rozgrywka")

# Czcionka do wyświetlania figur
font = pygame.font.Font(None, 36)

# Ścieżka do silnika
engine = chess.engine.SimpleEngine.popen_uci("pretty-fishy-ai")

# Tworzenie szachownicy
board = chess.Board()

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    # Figury
    piece_symbols = {
        chess.PAWN: 'P', chess.KNIGHT: 'N', chess.BISHOP: 'B', chess.ROOK: 'R', chess.QUEEN: 'Q', chess.KING: 'K'
    }
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)
                text = font.render(piece_symbols.get(piece.piece_type, '?'), True, FONT_COLOR)
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 3, row * SQUARE_SIZE + SQUARE_SIZE // 3))

def stockfish_move():
    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=1.0))
        board.push(result.move)
        print(f"Stockfish rusza: {result.move}")

def play_game():
    running = True
    
    if board.turn == chess.WHITE: # Pierwszy biały
        stockfish_move()
    
    while running:
        screen.fill((0, 0, 0))
        draw_board()
        draw_pieces()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        
        if board.turn == chess.WHITE:  # Pierwsze grają białe figury
            stockfish_move()
        else:
            move = input("Twój ruch (np. e2e4): ") # Ruch jest z e2 do e4
            try:
                chess_move = chess.Move.from_uci(move)
                if chess_move in board.legal_moves:
                    board.push(chess_move)
                    stockfish_move()
            except ValueError:
                print("Niepoprawny ruch")
    
    pygame.quit()
    engine.quit()

play_game()
